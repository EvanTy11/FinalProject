import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class plotdata:
    '''Class used for plotting data'''
    def createpieChart(self, query, connection,var):
        '''Creates a pie chart based on the query result'''
        with connection.session() as session:
            result = session.run(query ,value=var)
            data = [record[var] for record in result]

        connection.close()

        # Convert data to DataFrame
        df = pd.DataFrame(data, columns=[var])

        df[var].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title(f'Pie Chart of Vehicle Registration {var}')

        # Display the pie chart
        plt.axis('equal')
        plt.show()


    def createheatmap(self, query, connection, var, var2):
        '''Creates a heatmap based on the query result'''
        with connection.session() as session:
            result = session.run(query, value=var)
            data = [(record[var], record[var2]) for record in result]

        connection.close()

        # Convert data to DataFrame
        df = pd.DataFrame(data, columns=[var, var2])

        # Ensure x and y contain numeric values
        df[var] = pd.to_numeric(df[var], errors='coerce')
        df[var2] = pd.to_numeric(df[var2], errors='coerce')

        # Drop None values
        df.dropna(inplace=True)

        x_min, x_max = df[var].min(), df[var].max()
        y_min, y_max = df[var2].min(), df[var2].max()

        # Creates heatmap
        plt.figure(figsize=(12, 8))
        plt.hist2d(df[var], df[var2], bins=(np.linspace(x_min, x_max, 50), np.linspace(y_min, y_max, 20)), cmap='magma', norm=plt.Normalize(vmin=0, vmax=100))
        plt.colorbar(label='Frequency')
        plt.title('Electric Vehicle Population Heatmap')
        plt.xlabel(var)
        plt.ylabel(var2)
        plt.show()

    def createbarPlot(self, query, connection, var):
        '''Creates a bar plot based on the query result'''
        with connection.session() as session:
            result = session.run(query, value=var)
            data = [record[var] for record in result]

        connection.close()
        df = pd.DataFrame(data, columns=[var])


        vehicle_count_by_make = df[var].value_counts()

        # Create a bar plot
        plt.figure(figsize=(10, 6))
        vehicle_count_by_make.plot(kind='bar', color='skyblue')
        plt.title(f'Electric Vehicle Population by {var}')
        plt.xlabel(var)
        plt.ylabel('Number of Vehicles')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
