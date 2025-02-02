import requests

def fetch_youtube_videos():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos/EQwmQLU1S6I"
    response = requests.get(url)
    data = response.json()    
    if data.get("success") and "data" in data:
        video_data = data["data"]
        video_title = video_data["video"]["items"]["snippet"]["title"]
        custom_url = video_data["channel"]["info"]["customUrl"]
        publish_at= video_data["channel"]["info"]["publishedAt"]
        return video_title, custom_url,publish_at
    else:
        raise Exception("Failed to fetch data")
    
def main():
    try:
        video_title, custom_url,publish_at = fetch_youtube_videos()
        print(f"Video Title: {video_title}\nCustom URL: {custom_url}\n publishAT:{publish_at}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
