import requests
from bs4 import BeautifulSoup
import yt_dlp

def get_embedded_videos(url):
    # درخواست به وبسایت
    response = requests.get(url)

    # بررسی وضعیت درخواست
    if response.status_code != 200:
        print(f"Failed to access {url}")
        return []

    # تجزیه HTML وبسایت
    soup = BeautifulSoup(response.content, 'html.parser')

    # استخراج تمامی تگ‌های <div> که دارای خاصیت video-src هستند
    video_divs = soup.find_all('div', {'video-src': True})

    # استخراج لینک ویدئوها از خاصیت video-src
    video_links = []
    for div in video_divs:
        video_src = div.get('video-src')
        if video_src:
            video_links.append(video_src.split('?')[0])  # حذف پارامترهای اضافی از URL

    return video_links

def download_video(video_url, cookie_file):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[ext=mp4]',  # انتخاب کیفیت 720p و ادغام صدا و تصویر
        'outtmpl': '%(title)s.%(ext)s',  # ذخیره ویدئو با نام اصلی
        'writesubtitles': True,  # دانلود زیرنویس
        'writeautomaticsub': True,  # دانلود زیرنویس خودکار (اگر موجود باشد)
        'merge_output_format': 'mp4',  # فرمت خروجی mp4
        'cookiefile': cookie_file,  # استفاده از فایل کوکی‌های مرورگر برای عبور از محدودیت‌های یوتیوب
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print(f"Downloaded: {video_url}")
        except Exception as e:
            print(f"Failed to download {video_url}: {str(e)}")


if __name__ == "__main__":
    # آدرس سایت حاوی ویدئوها
    website_url = "https://www.testwebsite.com/ee/ee/ee"

    # مسیر فایل کوکی‌های استخراج شده از مرورگر Edge
    cookie_file = "path_to_your_cookies.txt"  # مسیر فایل کوکی

    # استخراج لینک‌های ویدئو از وبسایت
    video_links = get_embedded_videos(website_url)

    if video_links:
        print("Found video links:")
        for link in video_links:
            print(link)

        # دانلود ویدئوها همراه با زیرنویس‌های انگلیسی و عربی
        for video_link in video_links:
            download_video(video_link, cookie_file)
    else:
        print("No videos found.")