
# Factory

original_text = 'Hello! how are you todya? :)'

answer = find_answer(original_text)
if not answer:
    sanitized_text = make_ascii(original_text.lower())
    answer = find_answer(sanitized_text)
if not answer:
    answer = find_answer(typo_correct(original_text))
if not answer:
    san_and_typo_text = typo_correct(sanitized_text)
    answer = find_answer(san_and_typo_text)

return answer


original_text = 'Hello! how are you todya? :)'

text_factory = TextFactory(original_text)

answer = find_answer(original_text)
if not answer:
    answer = find_answer(text_factory.sanitized())
if not answer:
    answer = find_answer(text_factory.typo_corrected())
if not answer:
    answer = find_answer(text_factory.sanitized_and_typo_corrected())

return answer




class TextFactory:

    def __init__(self, text):
        self.original = text

    def sanitized(self):
        return make_ascii(self.original.lower())

    def typo_corrected(self):
        return typo_correct(self.raw)

    def sanitized_and_typo_corrected(self):
        return typo_correct(self.sanitized())



class TextFactory:

    def __init__(self, text):
        self.original = text

    def sanitized(self):
        if not self._sanitized:
            self._sanitized = make_ascii(self.original.lower())
        return self._sanitized

    def typo_corrected(self):
        if not self._typo_corrected:
            self._typo_corrected = typo_correct(self.original)
        return self._typo_corrected

    def sanitized_and_typo_corrected(self):
        if not self._sanitized_and_typo_corrected:
            self._sanitized_and_typo_corrected = typo_correct(self.sanitized())
        return self._sanitized_and_typo_corrected


# Facade

s3.write('some_s3_bucket', 'photos/user1234/photo.jpg.gz', gzip(photo))
youtube_api.put_video('chris', 'Video for User 1234', 'video1234.mp4')
s3.write('some_s3_bucket', 'meta/user1234/metadata.json',
        json.dumps(metadata))

...

photo = gunzip(s3.read('some_s3_bucket', 'photos/user1234/photo.jpg.gz'))
video = youtube_api.get_video('chris', 'Video for User 1234')
metadata = json.loads(s3.read('some_s3_bucket', 'meta/user1234/metadata.json'))

...




user_data_facade = UserDataFacade(1234)

user_data_facade.put_photo(photo)
user_data_facade.put_video(video)
user_data_facade.put_metadata(metadata)
...
photo = user_data_facade.get_photo()
video = user_data_facade.get_video()
metadata = user_data_facade.get_metadata()



class UserDataFacade:

    S3_BUCKET = 'some_s3_bucket'
    YOUTUBE_ACCOUNT = 'chris'

    def __init__(self, user_id):
        self.user_id = user_id

    def get_photo(self):
        return gunzip(s3.read('some_s3_bucket', 
            'photos/user{}}/photo.jpg.gz'.format(self.user_id)))

    def put_photo(self, corpus):
        s3.write('some_s3_bucket', 
            'photos/user{}/photo.jpg.gz'.format(self.user_id), gzip(photo))

    def get_video(self):
        return youtube_api.get_video('chris', 
            'Video for User {}'.format(self.user_id))

    def put_video(self):
        youtube_api.put_video('chris', 'Video for User {}'.format(self.user_id),
            'video{}.mp4'.format(self.user_id))

    def get_metadata(self):
        return json.loads(s3.read('some_s3_bucket', 
            'meta/user{}/metadata.json'.format(self.user_id)))

    def put_metadata(self, classifier):
        s3.write('some_s3_bucket', 'meta/user{}/metadata.json'.format(self.user_id),
            json.dumps(metadata))


# Decorator

def upload():

    start_time = time()

    upload_video()

    print("Finished uploading in {} secs".format(time() - start_time ))


@timer
def upload():
    upload_video()


def timer(func):

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time()
        value = func(*args, **kwargs)
        print("Finished {} in {} secs"
                .format(func.__name__, time() - start_time))
        return value
        
    return wrapper_timer    



# Summary

@timer
def upload(user_id):
    ...
    user_video = user_data_facade.get_video()
    
    user_video_factory = VideoTreatmentFactory(user_video)
    
    composed_video = CompositeVideoBuilder()
        .with_video(video_factory.black_and_white())
        .with_video(code_chrysalis_promo_video)
        .include_cut_scenes()
        .trim_to(seconds=45)
        .build()


