class Translation(object):
    START_TEXT = """Hi {},
I'm URL X Downloader! Send me direct link, I will upload it to Telegram for You!
/help for more details!"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "📥Downloading..."
    UPLOAD_START = "📤Uploading..."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using @UrlDownloaderZX_bot"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@UrlDownloaderZX_bot"
    SAVED_CUSTOM_THUMB_NAIL = "Custom image saved for thumbnail."
    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom thumbnail cleared succesfully✅."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """How to Use Me?
    /start - Check I'm alive or dead
    /help - How to use me
    /total - To get total users count(only admin)
    /viewthumbnail - Current Thumbnail
    /delthumbnail - Delete thumbnail
    
    Steps:
    1.Send me direct url (example.domain/File.mp4 | New Filename.mp4).
    2.Send Image As Custom Thumbnail (Optional).
    3.Select the button.
         SVideo-Give File as video with Screenshots
         SFile-Give File (video) as file with Screenshots
         Video-Give File as video without Screenshots
         File-Give File without Screenshots
If bot didn't respond, you can do nothing."""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. I'm cancelling it."

    ERROR_YTDLP = "Please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output."