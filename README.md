# 🏥 AI Smart Health Kiosk - Beginner's Guide

A simple machine learning project for first-year students to predict health risk based on vital signs.

## 📚 What This Project Does

This AI system takes 5 simple inputs:
- Age
- Temperature
- Heart Rate
- Blood Oxygen (SpO2)
- Number of symptoms

And predicts: **LOW, MODERATE, or HIGH** risk level

## 🛠️ Installation (Easy Steps!)

### Step 1: Install Python
Make sure you have Python installed (version 3.8 or higher).
Check by typing in terminal/command prompt:
```bash
python --version
```

### Step 2: Install Required Libraries
Open terminal/command prompt and type:
```bash
pip install pandas scikit-learn streamlit
```

That's it! Only 3 libraries needed.

## 🚀 How to Run (3 Simple Steps!)

### Step 1: Create Training Data
```bash
python create_dataset.py
```
This creates a file called `health_data.csv` with 500 sample patient records.

### Step 2: Train the AI Model
```bash
python train_model.py
```
This trains the AI and saves it as `health_model.pkl`. 
You should see accuracy around 90-95%!

### Step 3: Run the App
You have TWO options:

**Option A: Web Interface (Recommended)**
```bash
streamlit run app.py
```
A beautiful web page will open in your browser!

**Option B: Command Line**
```bash
python simple_checker.py
```
Simple text-based interface in your terminal.

## 📁 Project Files Explained

| File | What It Does |
|------|-------------|
| `create_dataset.py` | Makes fake health data for training |
| `train_model.py` | Trains the AI model |
| `app.py` | Web interface (looks nice!) |
| `simple_checker.py` | Terminal interface (basic) |
| `health_data.csv` | Training data (created automatically) |
| `health_model.pkl` | Trained AI model (created automatically) |

## 🎯 How the AI Works (Simple Explanation)

1. **Decision Tree**: The AI uses a "Decision Tree" - like a flowchart
2. **Learning**: It learns patterns from 500 example patients
3. **Prediction**: When you enter new data, it follows the flowchart to predict risk

Example of what the AI learns:
```
If temperature > 101°F AND SpO2 < 90% → HIGH RISK
If temperature > 99.5°F AND symptoms > 2 → MODERATE RISK
Otherwise → LOW RISK
```

## 🎨 Customization Ideas

Want to make it better? Try:

1. **Add more features**: Blood pressure, respiratory rate
2. **More data**: Change 500 to 1000 in `create_dataset.py`
3. **Different model**: Try `RandomForestClassifier` instead of `DecisionTreeClassifier`
4. **Colors**: Modify the Streamlit app colors
5. **Symptoms list**: Add checkboxes for specific symptoms

## 🐛 Common Problems & Solutions

**Problem**: "Module not found"
**Solution**: Run `pip install [module-name]`

**Problem**: "File not found: health_model.pkl"
**Solution**: Run steps in order! Create data first, then train model.

**Problem**: Web page won't open
**Solution**: Check if streamlit is installed: `pip install streamlit`

## 📊 Understanding the Accuracy

When you run `train_model.py`, you'll see something like:
```
Training accuracy: 95.2%
Testing accuracy: 92.8%
```

- **95.2%** means: AI got 95.2% correct on data it learned from
- **92.8%** means: AI got 92.8% correct on NEW data it never saw

**Good accuracy**: 85-95% ✅
**Too perfect**: 99-100% (might be overfitting) ⚠️
**Too low**: Below 75% (needs improvement) ❌

## 🎤 Hackathon Presentation Tips

When presenting your project:

1. **Demo First**: Show the working app immediately
2. **Explain Simply**: "It's like a smart flowchart that learned from examples"
3. **Show the Code**: Explain the 3 simple steps
4. **Mention AI**: "Using Decision Tree Machine Learning"
5. **Future Ideas**: "Could add more vitals, connect to real sensors"

### Key Points to Mention:
- ✅ Uses Machine Learning (Decision Tree)
- ✅ 90%+ accuracy
- ✅ Simple and fast
- ✅ Easy to understand
- ✅ Can be deployed to real kiosk with sensors

## 🔮 Next Steps (If You Have Time)

1. **Week 1-2**: Understand the basic code
2. **Week 3**: Try modifying the dataset
3. **Week 4**: Experiment with different models
4. **Week 5**: Improve the UI/design
5. **Week 6**: Add advanced features, practice presentation

## 💡 Learning Resources

- **What is Decision Tree?**: YouTube → "Decision Tree Explained Simply"
- **Streamlit Tutorial**: docs.streamlit.io
- **Python Pandas**: datacamp.com/tutorial/pandas
- **Scikit-learn**: scikit-learn.org/stable/tutorial/

## ❓ FAQ

**Q: Do I need to understand all the math?**
A: No! Just understand: Input → AI Model → Output

**Q: Can I use this for a real health kiosk?**
A: This is a prototype. Real medical AI needs much more data and approval.

**Q: What if I don't know Python well?**
A: That's okay! Just run the files in order and it works. Learn by experimenting.

**Q: How do I explain "pickle"?**
A: It's like saving your game progress - saves the trained model to load later.

## 🏆 Good Luck!

You've got this! This is a complete, working ML project. 
Run it, understand it, customize it, and present it with confidence!

Remember: Even simple ML can be impressive if you present it well! 🌟
