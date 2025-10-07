from flask import Flask,render_template,request
import numpy as np
import pickle

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           image = list(popular_df['Image-URL-M'].values),
                           votes = list(popular_df['num_ratings'].values),
                           rating = list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route("/recommend_books", methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    
    if user_input not in pt.index:
        return render_template('recommend.html', data=[], error="Book not found. Please try another title.")

    index = np.where(pt.index == user_input)[0][0]
    distances = similarity_scores[index]
    similar_items = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    data = []

    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')

        title = temp_df['Book-Title'].values[0]
        author = temp_df['Book-Author'].values[0]
        image_url = temp_df['Image-URL-M'].values[0]

        if isinstance(image_url, str):
            if image_url.startswith("http://"):
                image_url = image_url.replace("http://", "https://")
        else:
            image_url = ""

        item.extend([title, author, image_url])
        data.append(item)

    print(data)
    return render_template('recommend.html', data=data)

if __name__ == '__main__' :
    app.run(debug=True)
