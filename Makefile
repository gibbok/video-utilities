.PHONY: help extract compress report

help:
	@echo "Available targets:"
	@echo "  extract INPUT=<video> OUTPUT=<folder> [INTERVAL=5]  - Extract screenshots from video"
	@echo "  compress INPUT=<video> OUTPUT=<folder>              - Compress video to H265"
	@echo "  report FOLDER=<path> [OUTPUT=video_inventory.csv]   - Generate video inventory report"

extract:
	uv run extract_screenshots.py $(INPUT) $(OUTPUT) --interval $(or $(INTERVAL),5)

compress:
	uv run compress_h265.py $(INPUT) $(OUTPUT)

report:
	uv run video_report.py $(FOLDER) $(or $(OUTPUT),video_inventory.csv)
