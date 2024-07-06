# Food Demand Forecasting Model

## Overview
This project aims to forecast the demand for food items using a machine learning model. The model is trained on a dataset from Kaggle and deployed using a Flask web application to provide an interactive user experience.

## Dataset
The dataset for this project is sourced from Kaggle: [Food Demand Forecasting](https://www.kaggle.com/datasets/kannanaikkal/food-demand-forecasting). It includes information on the week, center ID, meal ID, prices, promotions, and number of orders.

## Files
- **index.html**: This HTML file is the front-end of the application where users input details to get predictions.
- **app.py**: This Python file contains the Flask web application code.
- **static/style.css**: CSS file for styling the HTML page.

## Installation
1. Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/food-demand-forecasting.git](https://github.com/Goutham-Senthil/Food-Forecasting-Model)
    ```
2. Navigate to the project directory:
    ```bash
    cd food-demand-forecasting
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```bash
    python app.py
    ```
2. Open your web browser and navigate to `http://127.0.0.1:5000`.
3. Enter the details of the food item in the form and submit to get the demand prediction.

## Features
- **Homepage Feature**: Specify if the food item is featured on the homepage.
- **Promotion**: Specify if the food item is listed under a promotion.
- **Area of Operation**: Input the area of operation in square kilometers.
- **Cuisine Type**: Select the type of cuisine (e.g., Indian, Italian, etc.).
- **City Code and Region Code**: Enter the city and region codes.
- **Category**: Choose the category of the food item (e.g., Biryani, Pizza, etc.).

## Example
Here's an example of how to use the form:
1. Select if the food item is featured on the homepage.
2. Select if the food item is under a promotion.
3. Enter the area of operation.
4. Choose the cuisine type.
5. Enter the city and region codes.
6. Select the category of the food item.
7. Click "Submit" to get the prediction.

## Contributing
Feel free to submit issues, fork the repository, and send pull requests. For major changes, please open an issue first to discuss what you would like to change.
