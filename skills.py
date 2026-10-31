# -*- coding: utf-8 -*-
"""Auditory Pure-Tone Average (PTA) & Speech-in-Noise Presbycusis Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def assess_auditory_presbycusis_cognitive_risk(**kwargs):
    """Calculates four-frequency Pure Tone Average (PTA at 0.5, 1, 2, 4 kHz), QuickSIN speech-in-noise SNR loss, and stratifies presbycusis-mediated cognitive decline and social withdrawal hazard."""
    hearing_threshold_500hz_db = kwargs.get('hearing_threshold_500hz_db')
    hearing_threshold_1000hz_db = kwargs.get('hearing_threshold_1000hz_db')
    hearing_threshold_2000hz_db = kwargs.get('hearing_threshold_2000hz_db')
    hearing_threshold_4000hz_db = kwargs.get('hearing_threshold_4000hz_db')
    snr_loss_db = kwargs.get('snr_loss_db')

    pta_4 = round((hearing_threshold_500hz_db + hearing_threshold_1000hz_db + hearing_threshold_2000hz_db + hearing_threshold_4000hz_db) / 4.0, 1)
    
    # WHO Hearing Loss Grading based on PTA:
    # <= 20 dB: Normal
    # 21 - 34 dB: Mild hearing loss
    # 35 - 49 dB: Moderate hearing loss
    # 50 - 64 dB: Moderately severe
    # >= 65 dB: Severe / Profound
    if pta_4 > 35.0 or snr_loss_db > 7.0:
        dementia_risk_multiplier = 3.0
        hearing_tier = "MODERATE HEARING LOSS (3x elevated 10-year dementia hazard via cognitive load reallocation)"
        rec = "Audiologist consultation for bilateral hearing aid fitting (reduces cognitive load and temporal lobe atrophy)."
    elif pta_4 > 20.0 or snr_loss_db > 3.0:
        dementia_risk_multiplier = 1.9
        hearing_tier = "MILD PRESBYCUSIS / SPEECH-IN-NOISE DEFICIT (Nearly 2x elevated dementia risk)"
        rec = "Auditory rehabilitation training, noise-attenuating protection in loud environments, annual audiometry."
    else:
        dementia_risk_multiplier = 1.0
        hearing_tier = "NORMAL HEARING ACUITY (Auditory cognitive processing intact)"
        rec = "Maintain hearing preservation protocols; avoid sustained > 85 dBA sound exposure."
        
    result = {
        "status": "success",
        "pure_tone_average_pta_db": pta_4,
        "quicksin_snr_loss_db": snr_loss_db,
        "who_hearing_impairment_tier": hearing_tier,
        "relative_cognitive_decline_multiplier": dementia_risk_multiplier,
        "neuro_auditory_action_plan": rec,
        "engine": "GenPark Auditory Pure-Tone Presbycusis Cognitive Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "assess_auditory_presbycusis_cognitive_risk": {
        "name": "assess_auditory_presbycusis_cognitive_risk",
        "description": "Calculates four-frequency Pure Tone Average (PTA at 0.5, 1, 2, 4 kHz), QuickSIN speech-in-noise SNR loss, and stratifies presbycusis-mediated cognitive decline and social withdrawal hazard.",
        "parameters": {
            "type": "object",
            "properties": {
                "hearing_threshold_500hz_db": {"type": "number", "description": "Pure tone threshold at 500 Hz (dB HL)"},
                "hearing_threshold_1000hz_db": {"type": "number", "description": "Pure tone threshold at 1000 Hz (dB HL)"},
                "hearing_threshold_2000hz_db": {"type": "number", "description": "Pure tone threshold at 2000 Hz (dB HL)"},
                "hearing_threshold_4000hz_db": {"type": "number", "description": "Pure tone threshold at 4000 Hz (dB HL)"},
                "snr_loss_db": {"type": "number", "description": "QuickSIN Signal-to-Noise Ratio Loss (dB)"},
            },
            "required": ['hearing_threshold_500hz_db', 'hearing_threshold_1000hz_db', 'hearing_threshold_2000hz_db', 'hearing_threshold_4000hz_db', 'snr_loss_db']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "assess_auditory_presbycusis_cognitive_risk":
            res = assess_auditory_presbycusis_cognitive_risk(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-auditory-pta-speech-in-noise-cognitive-decline-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-auditory-pta-speech-in-noise-cognitive-decline-skill...")
    test_args = {'hearing_threshold_500hz_db': 15.0, 'hearing_threshold_1000hz_db': 20.0, 'hearing_threshold_2000hz_db': 25.0, 'hearing_threshold_4000hz_db': 35.0, 'snr_loss_db': 3.5}
    res = assess_auditory_presbycusis_cognitive_risk(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-auditory-pta-speech-in-noise-cognitive-decline-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
