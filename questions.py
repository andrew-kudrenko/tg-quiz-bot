from typing import List, Optional, Union

import psycopg2


class Answer:
    def __init__(self, text: str, is_right: bool = False):
        self.text: str = text
        self.is_right: bool = is_right


class Question:
    def __init__(self, title: str, answers: List[Answer], explaining: Optional[str] = None):
        self.title: str = title
        self.answers: List[Answer] = answers

        if explaining:
            self.explaining: Optional[str] = explaining

        for i, answer in enumerate(answers):
            if answer.is_right:
                self.correct_answer_id: int = i
                break


class UserResult:
    def __init__(self, user_id: Union[str, int], right_answers: int):
        self.user_id: Union[str, int] = user_id
        self.right_answers: int = right_answers


class DB:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='quiz',
            user='postgres',
            password='postgres',
            host='localhost',
            port=7000
        )

        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_questions(self) -> List[Question]:
        self.cursor.execute('SELECT * FROM questions')
        records = self.cursor.fetchall()

        questions: list[Question] = []

        for record in records:
            answers: List[Answer] = []

            for answer in record[2]:
                answers.append(Answer(text=answer['text'], is_right=answer['is_right']))

            questions.append(Question(answers=answers, title=record[1], explaining=record[3]))

        return questions

    def save_user_result(self, r: UserResult):
        self.cursor.execute(f'INSERT INTO results(user_id, right_answers) VALUES ({r.user_id}, {r.right_answers});')


db = DB()
