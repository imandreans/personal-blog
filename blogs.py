import json
from datetime import datetime

class Blogs:
    def __init__(self, filename='blogs.json'):
        self.filename = filename

    def __fetch_blogs(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data

    def show_blogs(self):
        return self.__fetch_blogs()

    def add_blog(self, title, content):
        try:
            data = self.__fetch_blogs()
        except FileNotFoundError:
            data = []

        current_date = datetime.now()
        new_blog = {'id' : len(data) + 1,
                    'title' : title,
                    'publishing_date': current_date.strftime("%B %d, %Y"),
                    'content': content}
        data.append(new_blog)

        with open(self.filename, 'w') as file:
                json.dump(data, file, indent=2)

    def delete_blog(self, id: int):
        try:
            if int(id) <1:
                print("ID must be greater than 0")
            
            data = self.__fetch_blogs()
            data.pop(id-1)
            for i in range(len(data)):
                data[i]['id'] = i+1
            
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=2)
        except ValueError:
            print('Please input the ID you want to delete')
        except Exception as e:
            print(e)

    def update_blog(self, id:int, title: str, content: str):
        try:
            data = self.__fetch_blogs()
            data[int(id)-1]['title'] = title
            data[int(id)-1]['content'] = content

            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=2)
        except Exception as e:
            print(e)

    def display(self):
        for i in self.__fetch_blogs():
            print(i['id'], "=", i['title'])
if __name__ == '__main__':
    b = Blogs()
    b.display()
    b.update_blog(3, 'judul', 'isi')
    b.display()
    # b.delete_blog(2)
    # print('='*10)
    # b.display()