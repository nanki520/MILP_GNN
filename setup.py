from setuptools import setup

setup(
    name="MILP_GNN",
    version="1.0",
    description="Ablating a Graph Neural Network for Branching in Mixed Integer Linear Programming",
    author="Qi Chun",
    author_email="nankii_mo@163.com",
    packages=["MILP_GNN"],
    install_requires=["numpy", "pytorch"],
)
