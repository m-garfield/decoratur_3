from utils import logger
@logger('test.log')
def flat_generator(list_of_lists):
    for list_of_list_element in list_of_lists:
        for item in list_of_list_element:
            yield item