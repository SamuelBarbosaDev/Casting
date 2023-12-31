import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from DataUnderstanding import DataUnderstanding
from sklearn.preprocessing import scale


class DataVisualization(DataUnderstanding):
    def __init__(self) -> None:
        sns.set_theme(
            context='talk',
            style='ticks',
            font_scale=.8,
            palette='tab10',
            rc={
                'figure.figsize': (12, 8),
                'axes.grid': True,
                'grid.alpha': .2,
                'axes.titlesize': 'x-large',
                'axes.titleweight': 'bold',
                'axes.titlepad': 20,
            }
        )

        self.scatter_kwargs = dict(palette='viridis', alpha=0.8, linewidth=0)

    def gráfico_barplot(
        self,
        dataframe: pd.DataFrame,
        x: str,
        y: str,
        titulo: str = ''
    ):
        sns.barplot(
            data=dataframe,
            x=x,
            y=y
        )
        plt.title(titulo)
        plt.show()

    def gráfico_pairplot(
        self,
        dataframe: pd.DataFrame,
        titulo: str = '',

    ):
        sns.pairplot(dataframe)
        plt.title(titulo)
        plt.show()

    def gráfico_heatmap(
        self,
        dataframe: pd.DataFrame,
        titulo: str = '',
    ):
        sns.set(style='white')
        corr = dataframe.corr()
        plt.figure(figsize=(16, 10))
        sns.heatmap(
            corr, annot=True, cmap='RdBu_r', fmt='.2f', annot_kws={'size': 12}
        )
        plt.title(titulo)
        plt.show()

    def gráfico_boxplot(
        self,
        dataframe: pd.DataFrame,
        figsize: tuple,
        titulo: str = '',
    ):
        dataframe = dataframe.select_dtypes(include='number')
        dataframe = dataframe.apply(scale)
        fig = plt.figure(figsize=figsize)
        sns.boxplot(data=dataframe)
        plt.xticks(rotation=60, ha='right')
        plt.title(titulo)
        plt.show()

    def gráfico_boxplot_para_comparação_variáveis(
        self,
        dataframe: pd.DataFrame,
        figsize: tuple,
        x: str = '',
        y: str = '',
        titulo: str = ''
    ):
        fig = plt.figure(figsize=figsize)
        sns.boxplot(data=dataframe, x=x, y=y)
        plt.title(titulo)
        plt.show()

    def gráfico_histplot(
        self,
        dataframe: pd.DataFrame,
        coluna: str,
        titulo: str = '',
    ):
        sns.histplot(data=dataframe[coluna])
        plt.xticks(rotation=60, ha='right')
        plt.title(titulo)
        plt.show()

    def gráfico_scatterplot(
        self,
        dataframe: pd.DataFrame,
        x: str,
        y: str,
        hue: list,
        titulo: str = ''
    ):
        sns.scatterplot(data=dataframe, x=x, y=y, hue=hue)
        plt.title(titulo)
        plt.show()

    def gráfico_lineplot(
        self,
        dataframe: pd.DataFrame,
        x: str,
        y: str,
        titulo: str = ''
    ):
        sns.lineplot(data=dataframe, x=x, y=y)
        plt.xticks(rotation=45)
        plt.title(titulo)
        plt.show()

    def gráfico_linha_plot(
        self,
        data: pd.DataFrame,
        x: str,
        y: str,
        figsize: tuple = (10, 6),
        marker='o',
        linestyle='-',
        titulo: str = '',
        titulo_x: str = '',
        titulo_y: str = '',
    ):
        plt.figure(figsize=figsize)
        plt.plot(data[x], data[y], marker=marker, linestyle=linestyle)
        plt.xlabel(titulo_x)
        plt.ylabel(titulo_y)
        plt.title(titulo)
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    data_visualization = DataVisualization()
