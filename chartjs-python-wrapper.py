import json
import os
import time

class ChartJSWrapper:
    def __init__(self):
        self.chart_types = [
            "line", "bar", "radar", "doughnut", "pie", "polarArea", "bubble", "scatter"
        ]
        self.color_presets = {
            "blue": "rgba(54, 162, 235, 0.2)",
            "green": "rgba(75, 192, 192, 0.2)",
            "red": "rgba(255, 99, 132, 0.2)",
            "yellow": "rgba(255, 206, 86, 0.2)",
            "purple": "rgba(153, 102, 255, 0.2)",
            "orange": "rgba(255, 159, 64, 0.2)"
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, title):
        self.clear_screen()
        print("=" * 50)
        print(f"{title:^50}")
        print("=" * 50)
        print()

    def get_input(self, prompt, example="", default=None):
        if example:
            prompt += f" (e.g., {example})"
        if default:
            prompt += f" [Default: {default}]"
        user_input = input(prompt + ": ").strip()
        return user_input if user_input else default

    def get_list_input(self, prompt, example=""):
        return [item.strip() for item in self.get_input(prompt, example).split(",")]

    def get_color_input(self, prompt):
        print("\nAvailable color presets:")
        for color in self.color_presets:
            print(f"- {color}")
        print("Or enter a custom color (e.g., red, #FF0000, rgba(255,0,0,0.5))")
        
        color = self.get_input(prompt).lower()
        return self.color_presets.get(color, color)

    def get_data(self):
        labels = self.get_list_input("Enter labels (comma-separated)", "January,February,March")
        datasets = []
        dataset_count = 1

        while True:
            print(f"\n--- Dataset {dataset_count} ---")
            dataset = {}
            dataset["label"] = self.get_input("Enter dataset label", f"Dataset {dataset_count}")
            dataset["data"] = [float(x) for x in self.get_list_input("Enter data values (comma-separated)", "10,20,30")]
            dataset["backgroundColor"] = self.get_color_input("Enter background color")
            dataset["borderColor"] = self.get_color_input("Enter border color")
            dataset["borderWidth"] = int(self.get_input("Enter border width", "1", "1"))
            datasets.append(dataset)
            
            add_another = self.get_input("Add another dataset? (yes/no)", default="no").lower()
            if add_another != 'yes' and add_another != 'y':
                break
            dataset_count += 1

        return {"labels": labels, "datasets": datasets}

    def generate_chart(self):
        self.print_header("Chart Type Selection")
        print("Available chart types:")
        for i, chart_type in enumerate(self.chart_types, 1):
            print(f"{i}. {chart_type}")

        while True:
            try:
                choice = int(self.get_input("\nSelect chart type (enter number)", "1"))
                chart_type = self.chart_types[choice - 1]
                break
            except (ValueError, IndexError):
                print("Invalid choice. Please enter a number from the list.")

        self.print_header("Chart Configuration")
        chart_id = self.get_input("Enter chart ID (used in HTML)", "myChart")
        title = self.get_input("Enter chart title", "My Chart")
        
        self.print_header("Data Input")
        print("Now, let's input the data for your chart.")
        print("You'll need to provide labels and data values.")
        print("For example, if you're making a sales chart, labels might be months,")
        print("and data values might be sales figures for each month.")
        print("\nPress Enter when you're ready to continue...")
        input()

        data = self.get_data()

        js_code = f"""
        <canvas id="{chart_id}"></canvas>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script>
        const ctx = document.getElementById('{chart_id}');
        new Chart(ctx, {{
            type: '{chart_type}',
            data: {json.dumps(data)},
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{
                        position: 'top',
                    }},
                    title: {{
                        display: true,
                        text: '{title}'
                    }}
                }}
            }}
        }});
        </script>
        """

        return js_code

    def run(self):
        self.print_header("Welcome to the Chart.js Python Wrapper!")
        print("This tool will help you create JavaScript code for charts.")
        print("You'll be guided through each step with explanations and examples.")
        print("\nPress Enter to start...")
        input()

        while True:
            js_code = self.generate_chart()
            
            self.print_header("Generated JavaScript Code")
            print(js_code)
            print("\nThis code can be added to an HTML file to display your chart.")

            filename = self.get_input("\nEnter filename to save the chart (or press Enter to skip)")
            if filename:
                with open(filename, "w") as f:
                    f.write(js_code)
                print(f"Chart saved to {filename}")

            create_another = self.get_input("Would you like to create another chart? (yes/no)", default="no").lower()
            if create_another != 'yes' and create_another != 'y':
                break

        self.print_header("Thank you for using the Chart.js Python Wrapper!")
        print("Your charts have been created successfully.")
        print("Have a great day!")
        time.sleep(3)

if __name__ == "__main__":
    wrapper = ChartJSWrapper()
    wrapper.run()
