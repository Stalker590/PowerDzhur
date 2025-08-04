import requests


def get_ip_info(ip_address: str) -> dict:
    print(ip_address)
    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip_address}?fields=status,message,country,regionName,timezone,query")
        data = response.json()

        if data['status'] == 'fail':
            return {"error": data.get("message", "Unknown error")}

        return {
            "ip": data["query"],
            "country": data["country"],
            "region": data["regionName"],
            "timezone": data["timezone"]
        }

    except Exception as e:
        return {"error": str(e)}

