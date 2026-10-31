# Auditory Pure-Tone Average (PTA) & Speech-in-Noise Presbycusis Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `assess_auditory_presbycusis_cognitive_risk`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates four-frequency Pure Tone Average (PTA at 0.5, 1, 2, 4 kHz), QuickSIN speech-in-noise SNR loss, and stratifies presbycusis-mediated cognitive decline and social withdrawal hazard.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Auditory Neuro-Cognitive Longevity)`

## MCP Tool Specification
### `assess_auditory_presbycusis_cognitive_risk`
Parameters:
- `hearing_threshold_500hz_db` (float): Pure tone threshold at 500 Hz (dB HL)
- `hearing_threshold_1000hz_db` (float): Pure tone threshold at 1000 Hz (dB HL)
- `hearing_threshold_2000hz_db` (float): Pure tone threshold at 2000 Hz (dB HL)
- `hearing_threshold_4000hz_db` (float): Pure tone threshold at 4000 Hz (dB HL)
- `snr_loss_db` (float): QuickSIN Signal-to-Noise Ratio Loss (dB)

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-auditory-pta-speech-in-noise-cognitive-decline-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-auditory-pta-speech-in-noise-cognitive-decline-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
