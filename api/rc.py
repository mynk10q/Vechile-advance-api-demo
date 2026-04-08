import requests
import uuid
import json

def handler(request):
    try:
        # 🔹 GET param ?rc=HR26XXXX
        rc_number = request.args.get("rc")

        if not rc_number:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "RC number required"})
            }

        session_id = f"{uuid.uuid4()}-{uuid.uuid4()}"

        payload = {
            "regNo": rc_number.strip().upper(),
            "sessionid": session_id
        }

        headers = {
            "Content-Type": "application/json",
            "Origin": "https://www.91wheels.com",
            "Referer": "https://www.91wheels.com/",
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.post(
            "https://api1.91wheels.com/api/v1/third/rc-detail",
            headers=headers,
            json=payload,
            timeout=15
        )

        return {
            "statusCode": 200,
            "body": json.dumps(response.json())
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
