from django.conf.urls import patterns, url, include
from django.conf import settings

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import VideoSummaryList, VideoTranscripts

urlpatterns = patterns('public_api.video_outlines.views',
    url(
        r'^courses/{}$'.format(settings.COURSE_ID_PATTERN),
        VideoSummaryList.as_view(),
        name='video-summary-list'
    ),
    url(
        r'^transcripts/{}/(?P<block_id>[^/]*)/(?P<lang>[^/]*)$'.format(settings.COURSE_ID_PATTERN),
        VideoTranscripts.as_view(),
        name='video-transcripts-detail'
    ),
)

