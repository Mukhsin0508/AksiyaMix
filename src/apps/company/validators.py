import random
import string
import  os
import subprocess
import ffmpeg
from moviepy.editor import VideoFileClip

from django.core.exceptions import ValidationError
from django.db.models.expressions import result

from apps.company.models import *




def validate_unique_id(value):
    """ Validate unique id for the company """

    max_attempts = 100
    attempts = 0

    while Company.objects.filter(id_generate = value).exists():
        if attempts >= max_attempts:
            raise  ValidationError("Unable to generate a unique ID, Please try again! ")
        value = generate_unique_id()
        attempts += 1

    return value

def company_video_format(video):
    """ Validate Video format for the company """
    valid_video_extensions = ['.mp4', '.avi', '.mov', ]
    ext = os.path.splitext(video.name)[1]
    if ext.lower() not in valid_video_extensions:
        raise ValidationError("Unsupported file extension. Please upload a video in .mp4, .mov, or .avi format.")

def validate_video_size(video):
    """ Validate Company Video size
     The video file size should not exceed 2GB
    """
    # 2GB max size
    max_size = 5242880000
    if video.size > max_size:
        raise ValidationError("The video file size should not exceed 50MB")


def get_video_duration(video_path):
    """ Get video duration
    """
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", video_path],
        stdout=subprocess.PIPE, # get output
        stderr=subprocess.STDOUT, # get output
    )
    return float(result.stdout)

def validate_video_duration(video):
    """ Validate Company Vide Duration
    The video duration should not exceed 5 minutes
    """
    max_duration = 300 # 5 minutes
    duration = get_video_duration(video.file.path)
    if duration > max_duration:
        raise ValidationError("The video duration should not exceed 5 minutes")

def validate_video_resolution(video):
    """ Validate Company Video Resolution
    The video resolution should be up to 3840x2160 (4K UHD
    """
    max_width = 3840
    max_height = 2160
    clip = VideoFileClip(video.file.path)
    width, height = clip.size
    if width > max_width or height > max_height:
        raise ValidationError("The video resolution should be up to 3840x2160 (4K UHD)")

def validate_video_aspect_ratio(video):
    """ Validate Company Video Aspect Ratio
    The video aspect ratio should be 16:9
    """
    clip = VideoFileClip(video.file.path)
    width, height = clip.size
    aspect_ratio = width / height
    if not (aspect_ratio == 16/9):
        raise ValidationError("The video aspect ratio should be 16:9")

def get_video_audio_channels(video_path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a:0",
         "-show_entries", "stream=channels",
         "-of", "default=noprint_wrappers=1:nokey=1", video_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return result.stdout.strip()

def validate_audio_track(video):
    """ Validate Company Video Audio Track
    The video should have at least 1 audio track
    """
    audio_channels = get_video_audio_channels(video.file.path)
    if audio_channels:
        raise ValidationError("No audio track found in the video")
