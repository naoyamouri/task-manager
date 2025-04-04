from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    due_date = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='未完了')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form.get('description', '')
    due_date_str = request.form.get('due_date', '')
    
    due_date = None
    if due_date_str:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
    
    task = Task(title=title, description=description, due_date=due_date)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_status/<int:task_id>', methods=['POST'])
def update_status(task_id):
    task = Task.query.get_or_404(task_id)
    task.status = '完了' if task.status == '未完了' else '未完了'
    db.session.commit()
    return jsonify({'status': task.status})

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Cloud Run環境変数からポートを取得
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
