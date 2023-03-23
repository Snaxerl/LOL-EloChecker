import requests

# Set your API key here
API_KEY = "KEY"

# Set the base URL for the API
BASE_URL = "https://euw1.api.riotgames.com"

def get_summoner_by_name(summoner_name):
    # Format the URL for the API call
    url = f"{BASE_URL}/lol/summoner/v4/summoners/by-name/{summoner_name}"

    # Set the headers for the API call
    headers = {"X-Riot-Token": API_KEY}

    # Make the API call
    response = requests.get(url, headers=headers)

    # Check if the API call was successful
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    # Return the summoner data
    return response.json()

def get_ranked_stats_by_summoner_id(summoner_id):
    # Format the URL for the API call
    url = f"{BASE_URL}/lol/league/v4/entries/by-summoner/{summoner_id}"

    # Set the headers for the API call
    headers = {"X-Riot-Token": API_KEY}

    # Make the API call
    response = requests.get(url, headers=headers)

    # Check if the API call was successful
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    # Return the ranked stats data
    return response.json()

# Example usage of the functions
summoner_name = input("Enter a summoner name: ")
summoner_data = get_summoner_by_name(summoner_name)
if summoner_data:
    print(f"Summoner name: {summoner_data['name']}")
    print(f"Summoner level: {summoner_data['summonerLevel']}")

    ranked_stats_data = get_ranked_stats_by_summoner_id(summoner_data["id"])
    if ranked_stats_data:
        for stat in ranked_stats_data:
            print(f"{stat['queueType']}: {stat['tier']} {stat['rank']} ({stat['leaguePoints']} LP)")

