import numpy as np

# Project Settings

ACTIONS = [
    ("0", "동작 없음"),
    ("6045", "신기록"),
    ("6112", "수제비"),
    ("2673", "뽀뽀"),
    ("8229", "월세"),
    ("15526", "사용자"),
    ("2983", "빵집"),
    ("6215", "대화"),
    ("6857", "단추"),
    ("6994", "천국"),
    ("9024", "초등학교"),
    ("11864", "사과"),
    ("5581", "새해"),
    ("10961", "백조"),
    ("6565", "술집"),
    ("7064", "이발사"),
    ("10192", "정장"),
    ("6212", "대학교"),
    ("8382", "복습"),
    ("9228", "상장"),
    ("11823", "식장"),
    ("9794", "보석상"),
    ("8902", "(화학)실험"),
    ("1074", "혁신"),
    ("11801", "문법"),
    ("23969", "자비"),
    ("11519", "기타")
]


class Config:
    # MediaPipe Settings
    MIN_DECTION_CONFIDENCE = 0.5
    MIN_TRACKING_CONFIDENCE = 0.5

    # Train & Test
    VALID_FOLDER_VIDEO = "dataset/VV_Data"
    RECOGNIZE_THRESHOLD = 0.5

    # Videos_capture
    WAIT_TIME = 3
    SEQUENCE_LENGTH = 40
    VIDEO_FOLDER = "dataset/GV_Data"
    DATASET_DB_FILE = "dataset/dataset.db"
    VALIDSET_DB_FILE = "dataset/validset_khy.db"
    FPS = 10

    # OpenCV Settings
    CAMERA_WIDTH = 1280
    CAMERA_HEIGHT = 720

    @staticmethod
    def get_action_num():
        temp = [i[0] for i in ACTIONS]
        temp.sort(key=lambda x: int(x[0]))
        return np.array([i[0] for i in ACTIONS])

    @staticmethod
    def get_action_dict():
        return ACTIONS

    @staticmethod
    def get_action_name(action_num):
        for action in ACTIONS:
            if action_num == action[0]:
                return action[1]
