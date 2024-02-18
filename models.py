import csv
import json
from utils import download_files

profit_percentage = 15

class Product:

    # "Handle": "proyector-estrellado",
    # "Title": "Proyector estrellado colorido para niños. lámpara de noche romántica con Bluetooth. reproductor de música USB. luz nocturna de estrellas. regalo",
    # "Body": "Proyector estrellado colorido para niños, lámpara de noche romántica con Bluetooth, reproductor de música USB, luz nocturna de estrellas, regalo",
    # "Variant Price": "200.00",
    # "Cost per item": "200.00",
    
    def __init__(self, handle, title, body, variant_price, _cost_per_item) -> None:
        self.handle = handle.replace(",", "-").replace(" ", "-").lower()
        self.title = title.replace(",", "-")
        self.body = body.replace(",", "-")
        self.variant_price = variant_price
        self._cost_per_item = _cost_per_item
        

    def dict(self):
        return {
            "Handle": self.handle,
            "Title": self.title,
            "Body": self.body,
            "Variant Price": self.variant_price,
            "Cost per item": self._cost_per_item
        }

    def get_full_product(self):

        data = self.dict()

        with open('utils/model_product.json', 'r') as json_file:
             
            model_product = json.load(json_file)
            product = {**model_product, **data}
            return product
        
    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            handle = data["Handle"].replace(",", "-").replace(" ", "-").lower()
            title = data["Title"].replace(",", "-")
            body = data["Body"].replace(",", "-")
            variant_price = float( data["Variant Price"]) * 1/(1 - profit_percentage/100)
            _cost_per_item = float(data["Cost per item"]) * 1/(1 - profit_percentage/100)

            images = data["Images"]
            download_files(images, handle)

            return Product(handle, title, body, variant_price, _cost_per_item)


class Exporter:

    products = []

    def __init__(self) -> None:
        pass

    def add_product(self, product):
        self.products.append(product)

    def add_product(self):

        handle = input("Enter the handle: ")
        title = input("Enter the title: ")
        body = input("Enter the body: ")
        variant_price = input("Enter the variant price: ")
        _cost_per_item = input("Enter the cost per item: ")

        product = Product(handle, title, body, variant_price, _cost_per_item)

        self.products.append(product)

    def export_products(self, filename):
        products = [product.get_full_product() for product in self.products]
        with open("outputs/"+filename+".csv", 'w') as csv_file:

            headers = list(products[0].keys())
            writer = csv.writer(csv_file)

            writer.writerow(headers)
            for data in products:
                writer.writerow(data.values())

        print("Products have been exported.")

    def load_bulk_products(self):
        with open("load_bulk.json", 'r') as json_file:
            prods = json.load(json_file)
            for data in prods:
                
                handle = data["Handle"].replace(",", "-").replace(" ", "-").lower()
                title = data["Title"].replace(",", "-")
                body = data["Body"].replace(",", "-")
                variant_price = str(float( data["Variant Price"]) * 1/(1 - profit_percentage/100))
                _cost_per_item = str(float(data["Cost per item"]) * 1/(1 - profit_percentage/100))
                images = data["Images"]
                download_files(images, handle)
                self.products.append(Product(handle, title, body, variant_price, _cost_per_item))
        
        print("Products have been loaded.")


    def menu(self):

        option = -1

        while option != "4":
            
            print("1. Add product")
            print("2. Export products")
            print("3. Load from JSON file")
            print("4. Load Bulk products from JSON file")
            print("5. Exit")
            option = input("Enter an option: ")

            if option == -1:
                pass
            elif option == "1":
                self.add_product()
            elif option == "2":
                filename = input("Enter the filename: ")
                self.export_products(filename)
                print("Products have been exported.")
                break
            elif option == "3":
                filename = "load_manual.json"
                product = Product.load_from_json(filename)
                self.products.append(product)
            elif option == "4":
                self.load_bulk_products()
                self.export_products("bulk_products")
                break
            elif option == "5":
                break
            else:
                print("Invalid option")



