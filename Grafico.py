import matplotlib.pyplot as plt

def main():
    x_coord = [0, 1, 2, 3, 4]
    y_coord = [0, 3, 1, 5, 2]

    plt.plot(x_coord, y_coord)
    plt.title('Vendite per anno')
    plt.xlabel('Anno')
    plt.ylabel('Vendite')
    plt.xticks([0, 1, 2, 3, 4], ['2020', '2021', '2022', '2023', '2024'])
    plt.yticks([0, 1, 2, 3 ,4, 5], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
