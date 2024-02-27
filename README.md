Task 1: Cloning and Forking

1. Cloning a Repository:

  - Choose a public GitHub repository of interest (ADVANCED-_PORT_SCANNER).

  - Clone the repository to your local machine.

    git clone https://github.com/cicada0007/ADVANCED-_PORT_SCANNER.git

  - Explore the repository's structure, files, and history.


2. Forking a Repository:

  - Fork the same repository you cloned in Task 1 to your GitHub account.

  - Clone the forked repository to your local machine.

    git clone https://github.com/juma5917/ADVANCED_PORT_SCANNER.git


Task 2: Managing Branches

3. Creating and Switching Branches:

  - In your local repository, create a new branch.

    git branch feature-update

  - Switch to the newly created branch.

    git checkout feature-update


4. Making Changes and Committing:

  - Make changes to a file or add a new file.

    touch index.html
    git add index.html

  - Commit the changes to the branch.

    git commit -m "Adding a new file index.html"


5. Merging Changes:

  - Switch back to the main branch.

    git checkout main

  - Merge the changes from the `feature-update` branch into the main branch.

    git merge feature-update


Task 3: Handling Conflicts

6. Creating Conflicts:

  - In your forked repository, make changes to the same file that you modified in Task 4.

  - Commit the changes.


7. Resolving Conflicts:

  - Create a new branch to resolve the conflict.

  - Resolve the conflict manually in the file.

  - Commit the changes and merge the branch back into `main`.


Task 4: GitHub Pages

8. Enabling GitHub Pages:

  - In your forked repository, create a simple HTML file (e.g., `index.html`).

  - Enable GitHub Pages for the repository and set the source branch to `main`.


9. Accessing the Published Page:

  - Visit the GitHub Pages URL for your repository and verify that the HTML file is accessible online.


