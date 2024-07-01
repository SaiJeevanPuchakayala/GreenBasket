import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure Google Gemini 1.5 model
genai.configure(api_key="AIzaSyBO6yz_YVfGsqxS18bQXszCMkeVirpL2EA")

# Function to generate sustainable recipe suggestions
def generate_recipe_suggestions(cuisine, meal_type, people):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = (f"You are a culinary expert specializing in sustainable and eco-friendly recipes.\n"
              f"Suggest a sustainable {cuisine} {meal_type} recipe for {people} people using lower-carbon ingredients.\n"
              f"Provide the recipe name, step-by-step cooking instructions, and a list of ingredients with quantities.\n"
              f"Include emojis and format the output as follows:\n"
              f"### Recipe Name: [Recipe Name] 🍽️\n"
              f"**Ingredients**:\n"
              f"   - Item 1\n"
              f"   - Item 2\n"
              f"   - ...\n"
              f"**Instructions**:\n"
              f"   - Step 1\n"
              f"   - Step 2\n"
              f"   - ...\n"
              f"**Sustainability Notes**:\n"
              f"   - Note 1\n"
              f"   - Note 2\n")
    response = model.generate_content(prompt)
    return response.text

# Function to analyze nutritional impact
def analyze_nutritional_impact(grocery_items):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = (f"You are a nutrition expert.\n"
              f"Analyze the nutritional content of the following grocery items and suggest healthier alternatives with lower environmental impact:\n"
              f"{', '.join(grocery_items)}\n"
              f"Provide a breakdown of vitamins, minerals, calories, and suggest improvements.\n"
              f"Format the output as follows:\n"
              f"### Nutritional Analysis 🥗\n"
              f"1. **Item**: Calories, Vitamins, Minerals, etc.\n"
              f"2. **Suggestions**:\n"
              f"   - Alternative 1\n"
              f"   - Alternative 2\n")
    response = model.generate_content(prompt)
    return response.text

# Function to generate zero-waste meal kits
def generate_zero_waste_meal_kit(meal_type, dietary_preferences):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = (f"You are an expert in zero-waste cooking.\n"
              f"Suggest customizable zero-waste meal kits for {meal_type} considering the following dietary preferences: {dietary_preferences}.\n"
              f"Provide tips on how to minimize waste and use reusable or compostable packaging.\n"
              f"Format the output as follows:\n"
              f"### Eco-Friendly Meal Kit 🍱\n"
              f"1. **Meals**:\n"
              f"   - Meal 1\n"
              f"   - Meal 2\n"
              f"   - ...\n"
              f"2. **Tips**:\n"
              f"   - Tip 1\n"
              f"   - Tip 2\n")
    response = model.generate_content(prompt)
    return response.text

# Function to provide seasonal eating guide
def seasonal_eating_guide(location, month, season):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = (f"You are an expert in sustainable eating.\n"
              f"Provide a seasonal eating guide for {location} during {month} ({season} season).\n"
              f"Highlight in-season produce and suggest recipes that use these ingredients.\n"
              f"Explain the environmental benefits of eating seasonally.\n"
              f"Format the output as follows:\n"
              f"### Seasonal Eating Guide 🌱\n"
              f"1. **In-Season Produce**:\n"
              f"   - Produce 1\n"
              f"   - Produce 2\n"
              f"   - ...\n"
              f"2. **Recipes**:\n"
              f"   - Recipe 1\n"
              f"   - Recipe 2\n"
              f"3. **Benefits**:\n"
              f"   - Benefit 1\n"
              f"   - Benefit 2\n")
    response = model.generate_content(prompt)
    return response.text

# Function to transform leftovers into new meals
def transform_leftovers(leftover_ingredients):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = (f"You are a creative chef specialized in minimizing food waste.\n"
              f"Suggest creative recipes to transform the following leftover ingredients into new meals: {', '.join(leftover_ingredients)}.\n"
              f"Provide storage tips to keep leftovers fresh longer.\n"
              f"Format the output as follows:\n"
              f"### Leftover Transformation ♻️\n"
              f"1. **Recipes**:\n"
              f"   - Recipe 1\n"
              f"   - Recipe 2\n"
              f"   - ...\n"
              f"2. **Storage Tips**:\n"
              f"   - Tip 1\n"
              f"   - Tip 2\n")
    response = model.generate_content(prompt)
    return response.text

# Set the page style
st.markdown(
    """
    <style>
    .stApp {
        background-color: #013220;
        color: white;
    }
    div[data-testid="stSidebar"] {
        background-color: #013220;
    }
    .css-1d391kg p {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

## Initialize our Streamlit app
im = Image.open("./Images/food_analysis.png")
st.set_page_config(
    page_title="GreenBasket",
    page_icon=im,
)

# Streamlit app layout
st.title("GreenBasket 🌿 - Every Basket Counts and Makes an Impact on the Planet 🌍")

with st.sidebar:
    img = Image.open("./Images/food_analysis.png")
    st.image(img)
    st.subheader("About GreenBasket")
    st.write(
        "GreenBasket is an innovative and eco-friendly digital platform designed to promote sustainable living through conscious food choices. Our mission is to help individuals and families reduce their carbon footprint by making it easier to plan, prepare, and enjoy meals that are both delicious and environmentally responsible."
    )

st.write(
    "### Key Features:"
)
st.write(
    "1. **Sustainable Recipe Generator 🍽️**:\n"
    "- Generate recipes that use lower-carbon ingredients.\n"
    "- Provides step-by-step cooking instructions.\n"
    "- Focus on utilizing locally sourced and seasonally available produce.\n"
    "- Helps in reducing the overall environmental impact of your meals."
)
st.write(
    "2. **Nutritional Insights & Alternatives 🥗**:\n"
    "- Analyze the nutritional content of your grocery basket.\n"
    "- Suggest healthier and more sustainable alternatives.\n"
    "- Highlight the health benefits of reducing processed foods and increasing fresh produce intake.\n"
    "- Educates users about the nutritional value of their food choices."
)
st.write(
    "3. **Eco-Friendly Meal Kits 🍱**:\n"
    "- Offer customizable zero-waste meal kits.\n"
    "- Tailored to users' dietary preferences and needs.\n"
    "- Utilize reusable or compostable packaging.\n"
    "- Minimize food waste by providing exact portions needed for recipes."
)
st.write(
    "4. **Seasonal Eating Navigator 🌱**:\n"
    "- Encourage seasonal eating by highlighting in-season produce.\n"
    "- Suggest recipes that use ingredients available in your region and season.\n"
    "- Educate users on the environmental benefits of eating seasonally, such as reduced transportation emissions and supporting local farmers."
)
st.write(
    "5. **Leftover Culinary Creations ♻️**:\n"
    "- Transform leftovers into new, creative meals.\n"
    "- Reduce food waste by providing recipes that utilize ingredients you already have.\n"
    "- Offer storage tips to keep leftovers fresh longer."
)
st.write(
    "### Benefits of Using GreenBasket:"
)
st.write(
    "- **Environmental Impact**: By choosing recipes and meal kits that prioritize sustainable ingredients, users can significantly reduce their carbon footprint and contribute to a healthier planet.\n"
    "- **Health and Wellness**: The platform emphasizes nutritious and wholesome food choices, helping users to improve their overall health and well-being.\n"
    "- **Cost Efficiency**: By minimizing food waste and focusing on seasonal produce, users can save money on groceries.\n"
    "- **Convenience**: GreenBasket provides easy-to-follow recipes and meal planning tools, making it simple to incorporate sustainable eating habits into daily life.\n"
    "- **Education**: The platform educates users about the benefits of sustainable eating, helping to foster a greater awareness of the environmental impact of food choices."
)
st.write(
    "GreenBasket aims to be more than just a meal planning tool; it is a comprehensive guide to making eco-friendly and health-conscious food choices. Whether you're looking to reduce your carbon footprint, improve your diet, or simply find new and exciting recipes, GreenBasket is your go-to platform for all things sustainable and delicious."
)
st.write(
    "Join us in our journey to make every basket count and create a positive impact on our planet! 🌍🌿"
)

# Create the navigation tabs
tabs = st.tabs(["Sustainable Recipe Generator 🍽️", "Nutritional Insights & Alternatives 🥗", "Eco-Friendly Meal Kits 🍱", "Seasonal Eating Navigator 🌱", "Leftover Culinary Creations ♻️"])

# Sustainable Recipe Generator Tab
with tabs[0]:
    st.header("Sustainable Recipe Generator 🍽️")

    # User input for cuisine type, meal type, and number of people
    cuisine = st.text_input("Enter the cuisine type you want (e.g., Italian, Chinese) 🌍")
    meal_type = st.selectbox("Select meal type 🥘", ["Breakfast", "Lunch", "Dinner", "Snack"])
    people = st.number_input("Enter the number of people in the house 👥", min_value=1, step=1)

    if st.button("Generate Recipe Suggestions ✨"):
        if cuisine and meal_type and people:
            st.write("Generating recipe suggestions... 🍽️")
            recipe_suggestions = generate_recipe_suggestions(cuisine, meal_type, people)
            st.write("Recipe Suggestions:")
            st.markdown(recipe_suggestions, unsafe_allow_html=True)

# Nutritional Insights & Alternatives Tab
with tabs[1]:
    st.header("Nutritional Insights & Alternatives 🥗")

    # User input for grocery items
    grocery_items = st.text_area("Enter the grocery items you want to analyze (separate with commas, e.g., apples, bananas, chicken breast) 🛒")

    if st.button("Analyze Nutritional Impact 💡"):
        if grocery_items:
            st.write("Analyzing nutritional impact... 🥗")
            grocery_list = [item.strip() for item in grocery_items.split(",")]
            nutritional_analysis = analyze_nutritional_impact(grocery_list)
            st.write("Nutritional Analysis:")
            st.markdown(nutritional_analysis, unsafe_allow_html=True)

# Eco-Friendly Meal Kits Tab
with tabs[2]:
    st.header("Eco-Friendly Meal Kits 🍱")

    # User input for meal type and dietary preferences
    meal_type = st.selectbox("Select meal type for the kit 🍽️", ["Breakfast", "Lunch", "Dinner", "Snack"])
    dietary_preferences = st.text_area("Enter dietary preferences (e.g., vegetarian, gluten-free, vegan) 🌱")

    if st.button("Generate Eco-Friendly Meal Kits ♻️"):
        if meal_type and dietary_preferences:
            st.write("Generating eco-friendly meal kits... 🍱")
            zero_waste_kit = generate_zero_waste_meal_kit(meal_type, dietary_preferences)
            st.write("Eco-Friendly Meal Kits:")
            st.markdown(zero_waste_kit, unsafe_allow_html=True)

# Seasonal Eating Navigator Tab
with tabs[3]:
    st.header("Seasonal Eating Navigator 🌱")

    # User input for location, month, and current season
    location = st.text_input("Enter your location (e.g., New York, USA) 📍")
    month = st.selectbox("Select the current month 📅", 
                         ["January", "February", "March", "April", "May", "June", 
                          "July", "August", "September", "October", "November", "December"])
    season = st.selectbox("Select the current season ☀️❄️", ["Winter", "Spring", "Summer", "Fall"])

    if st.button("Get Seasonal Eating Guide 🌿"):
        if location:
            st.write("Generating seasonal eating guide... 🌱")
            seasonal_guide = seasonal_eating_guide(location, month, season)
            st.write("Seasonal Eating Guide:")
            st.markdown(seasonal_guide, unsafe_allow_html=True)
        else:
            st.write("Please enter your location 📍.")

# Leftover Culinary Creations Tab
with tabs[4]:
    st.header("Leftover Culinary Creations ♻️")

    # User input for leftover ingredients
    leftover_ingredients = st.text_area("Enter the leftover ingredients you have (separate with commas, e.g., rice, chicken, broccoli) 🍲")

    if st.button("Transform Leftovers 🌟"):
        if leftover_ingredients:
            st.write("Generating recipes to transform leftovers... ♻️")
            leftovers_list = [ingredient.strip() for ingredient in leftover_ingredients.split(",")]
            leftover_recipes = transform_leftovers(leftovers_list)
            st.write("Leftover Recipes:")
            st.markdown(leftover_recipes, unsafe_allow_html=True)
