# **Blue Brain Open Platform** - Documents

This is a work-in-progress repository containing the [Architecture Documentation](docs/) of the **Blue Brain Open Platform**, as well as the review documents for the [AWS Well-Architected Framework](waf)[^waf_clarification].

For convenience, the file format utilized for the documentation is [Markdown](https://en.wikipedia.org/wiki/Markdown), and for the diagrams is Scalable Vector Graphics (SVG) made with [Draw.io](https://github.com/jgraph/drawio). The plan would be to either publish a GitHub Page at some point, or to generate a proper documentation via other means.

[^waf_clarification]: **Important:** The AWS Well-Architected Framework is expected to be followed inside the AWS Console instead.

## How to Edit the Documentation and Diagrams
One of the main reasons behind choosing the Markdown + Draw.io formats, is the convenience of having automatically available VSCode on GitHub for the very same repository. No installations nor complex configurations are required.

**To edit any of the files, including the diagrams, you must simply access the following link to open VSCode:**

> https://github.dev/BlueBrain/platform-docs

The repository contains a `.vscode` folder with a recommendation to enable the [Draw.io plugin for VSCode](https://www.drawio.com/blog/edit-diagrams-with-github-dev). Simply click on `Install` when prompted in the bottom-right of your screen, and from now on you will be able to edit any of the Draw.io figures inside GitHub.

> [!TIP]
> You can also clone the repository locally and utilize your own installation of VSCode. The same plugins are available in both versions.

> [!WARNING]
> Please, use **always** SVG file format while working with new figures. Name the files as `*.drawio.svg` for the plugin to automatically detect the Draw.io files in VSCode.
