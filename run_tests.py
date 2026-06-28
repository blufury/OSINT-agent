"""Batch runner: execute OSINTAgent on 5 test entities and save all outputs to runs/."""

import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

load_dotenv()

TEST_ENTITIES = [
    "Anthropic",
    "OpenAI",
    "Mistral AI",
    "Hugging Face",
    "LangChain",
]

OUTPUT_DIR = Path("runs")
console = Console()


def check_env() -> bool:
    missing = [k for k in ["ANTHROPIC_API_KEY", "TAVILY_API_KEY"] if not os.environ.get(k)]
    if missing:
        console.print(f"[red]Missing env vars: {', '.join(missing)}[/red]")
        console.print("Copy .env.example to .env and fill in your API keys.")
        return False
    return True


def run_entity(entity: str) -> dict:
    from osint_agent.graph import build_graph
    from osint_agent.state import AgentState

    start = time.time()
    graph = build_graph()
    try:
        result = graph.invoke(AgentState(seed_entity=entity))
        elapsed = time.time() - start
        return {
            "entity": entity,
            "success": True,
            "elapsed_s": round(elapsed, 1),
            "report": result.get("report", ""),
            "execution_log": result.get("execution_log", []),
            "tool_results_count": len(result.get("tool_results", [])),
        }
    except Exception as exc:
        elapsed = time.time() - start
        return {
            "entity": entity,
            "success": False,
            "elapsed_s": round(elapsed, 1),
            "error": str(exc),
            "report": "",
            "execution_log": [],
            "tool_results_count": 0,
        }


def save_run(run: dict) -> None:
    safe = run["entity"].replace(" ", "_").lower()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if run["report"]:
        (OUTPUT_DIR / f"{safe}_report.md").write_text(run["report"], encoding="utf-8")

    summary = {k: v for k, v in run.items() if k != "report"}
    (OUTPUT_DIR / f"{safe}_log.json").write_text(
        json.dumps(summary, indent=2, default=str), encoding="utf-8"
    )


def main() -> None:
    if not check_env():
        sys.exit(1)

    console.print(Panel(
        f"[bold cyan]OSINTAgent Batch Runner[/bold cyan]\n"
        f"Running {len(TEST_ENTITIES)} entities -> [dim]{OUTPUT_DIR}/[/dim]"
    ))

    results = []
    for i, entity in enumerate(TEST_ENTITIES, 1):
        console.print(f"\n[bold]({i}/{len(TEST_ENTITIES)})[/bold] Researching [yellow]{entity}[/yellow]...")
        run = run_entity(entity)
        save_run(run)
        results.append(run)

        status = "[green]OK[/green]" if run["success"] else "[red]FAIL[/red]"
        console.print(f"  {status} — {run['elapsed_s']}s — {run['tool_results_count']} tool results")
        if not run["success"]:
            console.print(f"  [red]Error:[/red] {run.get('error', '')}")

    # Summary table
    table = Table(title="Run Summary", show_lines=True)
    table.add_column("Entity")
    table.add_column("Status")
    table.add_column("Time (s)")
    table.add_column("Tools run")
    for r in results:
        table.add_row(
            r["entity"],
            "OK" if r["success"] else "FAIL",
            str(r["elapsed_s"]),
            str(r["tool_results_count"]),
        )
    console.print("\n")
    console.print(table)

    successes = sum(1 for r in results if r["success"])
    console.print(f"\n[bold]{successes}/{len(results)} runs succeeded.[/bold] Outputs in [dim]{OUTPUT_DIR}/[/dim]")


if __name__ == "__main__":
    main()
