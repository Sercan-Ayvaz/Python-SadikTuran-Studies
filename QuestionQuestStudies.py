#*********************** Questions-Quiz App ***********************

# Soru Sınıfı
class Question:
    def __init__(self,text,choices,answer):# Yapıcı Method
        self.text = text
        self.choices = choices
        self.answer = answer
    # Kullanıcı girdisini kontrol eden method.
    def checkAnswer(self,answer):
        return (self.answer).lower() == (answer.strip()).lower()
  

# Quiz uygulması
class Quiz:
    def __init__(self, questions):# Yapıcı method
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0
    
    # Mevcut soruyu döndürür.     
    def getQuestion(self):
        return self.questions[self.questionsIndex]
    
    # Mevcut soruyu ve seçenkleri ekrana yazdırır.
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Questions {self.questionsIndex + 1}: {question.text}')
        
        for q in question.choices:
            print(f'-{q}')
            
        answer = input("Answer: ")        
        self.guess(answer)
        self.loadQuestions()
    
    # Kullanıcının cevabını kontrol eder.
    def guess(self, answer):
        question = self.getQuestion()  
        
        if(question.checkAnswer(answer)):
            self.score += 1
        self.questionsIndex += 1
    
    # Tüm sorular bitmişse puanı gösterir, değilse sonraki soruya geçer.        
    def loadQuestions(self):
        if len(self.questions) == self.questionsIndex:    
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()    
    
    # Kullanıcının puanını gösterir.        
    def showScore(self):
        print('Score: ', self.score)
    
    # Kullanıcın ilerlemesini gösterir.        
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionsNumber = self.questionsIndex +1
        
        if questionsNumber > totalQuestion:
            print('Quiz End!')
        else:
            print(f' Quesiton {questionsNumber} of {totalQuestion} '.center(100,'*'))  
             
# Soru nesnelerinin oluşturulması.        
q1 = Question("Which is the best programming language?",['C#','Python','Javascript','Java'],'Python')
q2 = Question("Which is the most popular programming language?",['Python','Javascript','C#','Java'],'Python')
q3 = Question("Which is the most profitable programming language?",['C#','Javascript','Java','Python'],'Python')
q4 = Question("Which is the most popular programming language?",['C#','Javascript','Java','Python'],'Python')
q5 = Question("Which is the easiest programming language?",['C#','Javascript','Java','Python'],'Python')

# Soru listesinin oluşturulması.
questionList = [q1,q2,q3,q4,q5]

# Quiz nesnesini oluşturma ve başlatma.
quiz = Quiz(questionList)
quiz.loadQuestions()