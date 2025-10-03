# Code Toolbox

Code toolbox is a workspace designed to support the devolopment activities using a variety of tools. Its configuration allows, in particular, for choosing

- **resource configuration** including the number of CPUs, memory size, disk size, and whether GPU-based node should be used (if available)
- **software configuration** including the support for JetBrains tools integration (e.g., IDEA, PyCharm, etc), Python version.

Each toolbox is by default shipped with the **Jupyter notebook** support, VS Code Desktop integration (via preconfigured agent and VS Code extension), 
VS Code Web support. 

[Jupyter](https://jupyter.org/) is a web-based environment for interactive computing, ideal for testing and prototyping. Some of its main features are:

- Several programming languages supported: *Python*, *R*, *Julia*, *C++*, *Scala*...
- Collaborative development environment
- Mix code snippets with markdown-based documentation, charts and graphs

!!! info "How to access"

    Jupyter may be launched from [Coder, using its template](../tasks/workspaces.md). It will ask for the *CPU cores*, *GB of memory* and *GB of disk space* you wish to dedicate to it. Depending on the computation you need, lower values may turn out to be insufficient, but cores and memory may be changed even while the workspace is running.
    After launching it from Coder you can access Jupyter Notebook on [jupyter-notebook UI (http://nodeipaddress:30040)](http://nodeipaddress:30040).

## Writing a simple notebook

When you open Jupyter, the *Launcher* tab should appear, from which you can create a *Python 3* notebook. Once clicked, you can already start writing code.
Alternatively, you can also create a notebook by right-clicking within the *File Browser* to the left and choosing *New Notebook*.

Type some simple code, like `print('Hello world!')` and press *Shift+Enter*. Jupyter displays the result of the computation immediately under the code cell and creates a new one.

![Jupyter image](../images/jupyter.png)

You can change the type of a cell by clicking on the drop-down button (*Code*) at the top of your notebook. By choosing *Markdown*, you can alternate code and its documentation.

## Resources

- [Official documentation](https://jupyterlab.readthedocs.io/en/latest/)