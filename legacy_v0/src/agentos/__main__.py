from agentos.config.loader import default_loader
import sys

def main():
    print("AgentOS Starting...")
    try:
        constitution, decision_style, approval_matrix = default_loader.load_all()
        print(f"Loaded Constitution: {constitution.name}")
        print(f"Loaded Decision Style: {decision_style.name}")
        print(f"Loaded Approval Matrix: {approval_matrix.name}")
        print("Configuration valid. System ready (stub).")
    except Exception as e:
        print(f"Startup Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
