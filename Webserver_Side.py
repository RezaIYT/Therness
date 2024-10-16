# import requests
# from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
# import sys
# import tempfile
# import os
# from PySide6.QtGui import QPixmap
# import matplotlib.pyplot as plt



# import plotly.graph_objs as go



# # Replace with your EC2 instance's public IP or DNS
# EC2_URL = 'http://ec2-54-156-76-82.compute-1.amazonaws.com:5000/calculate'

# def send_data_to_server(data):
#     response = requests.post(EC2_URL, json=data, timeout=10)
#     return response.json()

# # Example usage
# data = {'value': 10}
# result = send_data_to_server(data)
# print('Result from server:', result)
# # PySide6 application code to send data to the server and display the result

# class ClientApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
        
#         self.R = []
#     def initUI(self):
#         self.layout = QVBoxLayout()

#         self.input_label = QLabel('Enter value:')
#         self.layout.addWidget(self.input_label)

#         self.input_field = QLineEdit(self)
#         self.layout.addWidget(self.input_field)

#         self.send_button = QPushButton('Send to Server', self)
#         self.send_button.clicked.connect(self.send_data)
#         self.layout.addWidget(self.send_button)

#         self.result_label = QLabel('Result from server will be shown here')
#         self.layout.addWidget(self.result_label)

#         self.setLayout(self.layout)
#         self.setWindowTitle('Client Application')

#     def send_data(self):
#         value = self.input_field.text()
#         if value:
#             data = {'value': int(value)}
#             result = send_data_to_server(data)
#             self.result_label.setText(f'Result from server: {result["result"]}')
#             self.R = result["result"]
            
#             self.ploydat()
            
            
#     def ploydat(self):
        
#         fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers', text=[f'Point {i}' for i in range(len(x))]))

#         # Update layout for better visualization
#         fig.update_layout(
#         title='Interactive Linear Plot',
#         xaxis_title='X Axis',
#         yaxis_title='Y Axis'
#         )

#         # Update the QLabel with the plot data

        
#         data = fig.data[0]
#         x = data.x
#         y = data.y
#         text = data.text

#         # Format the data as a string
#         data_str = "\n".join([f"{text[i]}: ({x[i]}, {y[i]})" for i in range(len(x))])

#         # Update the QLabel with the formatted data
#         self.data_label.setText(data_str)
        
        

       
        

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     client_app = ClientApp()
#     client_app.show()
#     sys.exit(app.exec())
    
    
    
    
    
    

    
    


import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class CalculationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label = QLabel("Enter a number:")
        self.layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        self.layout.addWidget(self.input_field)

        self.result_label = QLabel("Result will be shown here")
        self.layout.addWidget(self.result_label)

        self.button = QPushButton("Send to Cloud")
        self.button.clicked.connect(self.send_data_to_cloud)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
        self.setWindowTitle("Cloud Calculation App")
        self.show()

    def send_data_to_cloud(self):
        input_data = float(self.input_field.text())

        # Send data to the Azure API
        response = requests.post("https://therness-g4bgdybrhde0aqgb.italynorth-01.azurewebsites.net/calculate/", json={"input_data": input_data})

        if response.status_code == 200:
            result = response.json().get("result")
            self.result_label.setText(f"Result: {result}")
        else:
            self.result_label.setText("Error: Could not fetch result")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CalculationApp()
    sys.exit(app.exec())


