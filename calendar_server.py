import subprocess
from mcp.server.fastmcp import FastMCP
from datetime import datetime, timedelta

# Create the MCP server
mcp = FastMCP("Calendar Assistant")

def run_applescript(script: str) -> str:
    """Run an AppleScript command on macOS."""
    try:
        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            text=True
        )
        return result.stdout.strip() if result.stdout else "Done."
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def add_event(title: str, date: str, time: str, duration: int = 60) -> str:
    """
    Add an event to the default Calendar named 'Calendar'.
    Args:
        title: Title of the event
        date: Date in format YYYY-MM-DD
        time: Time in format HH:MM (24h)
        duration: Duration in minutes (default 60)
    """
    try:
        start_dt = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        end_dt = start_dt + timedelta(minutes=duration)

        # AppleScript date components
        start_script = f"""
        set startDT to current date
        set year of startDT to {start_dt.year}
        set month of startDT to {start_dt.strftime('%B')}
        set day of startDT to {start_dt.day}
        set hours of startDT to {start_dt.hour}
        set minutes of startDT to {start_dt.minute}

        set endDT to startDT + {duration*60} -- duration in seconds
        """

        script = f"""
        tell application "Calendar"
            tell calendar "Calendar"
                {start_script}
                make new event with properties {{summary:"{title}", start date:startDT, end date:endDT}}
            end tell
        end tell
        """

        return run_applescript(script)

    except Exception as e:
        return f" Failed to add event: {e}"



if __name__ == "__main__":
    mcp.run(transport="stdio")
