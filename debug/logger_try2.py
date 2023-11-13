import logging

# log 생성
logger = logging.getLogger("이 부분의 로그를 보자!")

# log level
logger.setLevel(logging.DEBUG)

# 콘솔, 파일 둘 다 떨궈보자
streamHandler = logging.StreamHandler()
fileHandler = logging.FileHandler("./server.log")
streamHandler.setLevel(logging.DEBUG)  # 로거 레벨에 맞추어 수정
fileHandler.setLevel(logging.DEBUG)

# formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s -  %(message)s'    
)

streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 핸들러 최종 추가
logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

def find_error_test():
    logger.debug('debug!!!')
    logger.info('info!!!')
    logger.warning('warning!!!')
