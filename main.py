if __name__ == '__main__':
    from data_loader import DataLoader
    from data_analyzer import DataAnalyzer
    from data_visualizer import DataVisualizer

    loader = DataLoader()
    data = loader.load_data()

    analyzer = DataAnalyzer(data)

    print("=== 基础统计分析 ===")
    print(analyzer.basic_statistics())

    print("\n=== 站点分析 ===")
    print(analyzer.location_analysis())

    print("\n=== 空气质量评估 ===")
    print(analyzer.air_quality_assessment())

    print("\n=== 温度极值分析 ===")
    print(analyzer.temperature_extremes())

if __name__ == '__main__':
    from data_loader import DataLoader

    loader = DataLoader()
    data = loader.load_data()

    visualizer = DataVisualizer(data)
    visualizer.plot_time_series()
    visualizer.plot_distribution()
    visualizer.plot_correlation()