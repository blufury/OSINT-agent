"""OSINTAgent CLI entry point."""

import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

load_dotenv()

console = Console()


def run(seed_entity: str, output_dir: str | None = None) -> None:
    from osint_agent.graph import build_graph
    from osint_agent.state import AgentState

    console.print(Panel(f"[bold cyan]OSINTAgent[/bold cyan]\nTarget: [yellow]{seed_entity}[/yellow]"))

    graph = build_graph()
    initial_state = AgentState(seed_entity=seed_entity)

    with console.status("[bold green]Running agent..."):
        result = graph.invoke(initial_state)

    # Display report
    console.print("\n")
    console.print(Markdown(result["report"]))

    # Save outputs
    if output_dir:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        safe_name = seed_entity.replace(" ", "_").lower()
        report_path = out / f"{safe_name}_report.md"
        log_path = out / f"{safe_name}_log.json"

        report_path.write_text(result["report"], encoding="utf-8")
        log_path.write_text(
            json.dumps(result["execution_log"], indent=2, default=str),
            encoding="utf-8",
        )
        console.print(f"\n[dim]Report saved to {report_path}[/dim]")
        console.print(f"[dim]Execution log saved to {log_path}[/dim]")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="OSINTAgent — Autonomous Open-Source Intelligence Research Assistant"
    )
    parser.add_argument("entity", help="Seed entity to research (org name, domain, GitHub handle)")
    parser.add_argument("--output", "-o", help="Directory to save report and logs", default=None)
    args = parser.parse_args()

    missing_keys = [k for k in ["ANTHROPIC_API_KEY", "TAVILY_API_KEY"] if not os.environ.get(k)]
    if missing_keys:
        console.print(f"[red]Missing required environment variables: {', '.join(missing_keys)}[/red]")
        console.print("Copy .env.example to .env and fill in your API keys.")
        sys.exit(1)

    run(args.entity, args.output)


if __name__ == "__main__":
    main()
