import requests
import uuid
import json

def handler(request):
    try:
        # ✅ query params (safe way)
        query = request.query
        rc = query.get("rc")

        if not rc:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "RC parameter required"})
            }

        rc = rc.upper()

        payload = {
            "regNo": rc,
            "sessionid": str(uuid.uuid4())
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

        data = response.json()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "success": True,
                "rc": rc,
                "data": data
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }
