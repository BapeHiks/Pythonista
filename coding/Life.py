#!python2
# coding: utf-8
# https://forum.omz-software.com/topic/2291/share-code-for-beginners-like-me-the-python-help-function


class SolveTheWorldsProblems(object):
    '''
    Description:
        это невозможно
        
    Args:
        смысл жизни
            
    Returns:
        -optimisim 
        
    Raises:
        больше вопросов, на которые можно ответить
    '''
    def __init__(self, meaning_of_life):
        '''
            комментарий для метода __init__
        '''
        self.meaning_of_life = meaning_of_life
        
    def result(self):
        '''
            комментарий к методу результата
        '''
        return ('optimism')
        
    

if __name__ == '__main__':
    stwp = SolveTheWorldsProblems(666)
    print help(stwp)
