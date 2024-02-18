# Shopify Dropshipping Automation Tool for AliExpress Products

This tool automates the process of adding new products from AliExpress into a Shopify store.

## Usage:

1. **Clone the Repository**: Clone the repository from [GitHub](https://github.com/xd860xd/shopify-dropshiping-automation-add-products.git).

2. **Install Dependencies**: Navigate to the root directory and install dependencies with Python using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Extract Data from AliExpress**:
    1. Go to the URL of the AliExpress product you want to add to your Shopify store.
    2. Open devtools and access the console.
    3. Paste the code line specified in `./utils/scrapper.js` into the console.

4. **Add Products to JSON File**:
    - After pasting the mentioned JavaScript code, the console will print a JSON.
    - Add this JSON data inside the `load_bulk.json` file.
    - You can add as many products as needed inside the `load_bulk.json` file.

5. **Run the Main Script**:
    - Activate your virtual environment.
    - Run the main script:
        ```bash
        python __init__.py
        ```
    - Select the 4th option: "Load Bulk products from JSON file" (type 4 and press Enter).
    - The tool will start downloading the images of the products and will create a `bulk_products.csv` file inside the `./outputs` directory.

6. **Import Products into Shopify**:
    - Upload the `bulk_products.csv` file in the "Import Products" section of Shopify.
    - Initially, products will not have any images. You'll need to upload them for each product, which is easy to do since all images are already in the `./output` directory.

## Prerequisites:
- Python installed
- Virtual environment set up

## Troubleshooting:
- If you encounter any errors during setup or execution, refer to the troubleshooting section in the repository or reach out for support.

## Security Considerations:
- Ensure that sensitive data, such as API keys or login credentials, are stored securely and not exposed in the repository.
- Follow Shopify's security best practices when integrating with your store.

## Feedback and Contributions:
- Your feedback is valuable! Feel free to report bugs, suggest improvements, or contribute code to the project. Visit the repository on GitHub to get involved.
