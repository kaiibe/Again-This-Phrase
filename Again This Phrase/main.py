from youtube_transcript_api import YouTubeTranscriptApi as YTA


def getVideoApi():

    while True:
        try:
            video_url = input('\nPlease pase an URL of a youtube video with subtitles: ')
            video_api = ''

            for i in range(0, len(video_url)):
                if video_url[i] == "=":
                    video_api = video_url[i + 1:]
                    break

            YTA.get_transcript(video_api)
            return video_api

        except:
            print("\nA youtube video is NOT valid or doesn't have a sub-titles, please try again!")



def getVideoTranscript(video_api):
    transcript = ''

    for value in video_api:
        for key, val in value.items():
            if key == 'text':
                val = val.lower()
                transcript += val

    split_lines = transcript.splitlines()
    final_transcript = " ".join(split_lines)
    return final_transcript



def countNumberOfRepetition(final_transcript):
    phrase = input("Please enter any word/phrase: ")
    phrase = phrase.lower()

    number_of_repetition = final_transcript.count(phrase)

    print("\nA phrase '" + phrase + "' was repeated in this video", number_of_repetition, 'times.')



def main():
    video_api = getVideoApi()
    data = YTA.get_transcript(video_api)
    final_transcript = getVideoTranscript(data)
    countNumberOfRepetition(final_transcript)

    # file = open("transcript", "w")
    # file.write(final_transcript)
    # file.close()



if __name__ == '__main__':
    main()