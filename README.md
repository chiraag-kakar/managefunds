# managefunds
A full stack funds management web app.

![](https://github.com/chiraag-kakar/managefunds/blob/master/banner.png)


[![](https://img.shields.io/github/license/chiraag-kakar/managefunds?style=for-the-badge)]()
[![](https://img.shields.io/tokei/lines/github/chiraag-kakar/managefunds?label=Lines%20of%20Code&style=for-the-badge)]()
[![](https://img.shields.io/github/issues-raw/chiraag-kakar/managefunds?color=orange&style=for-the-badge)]()
[![](https://img.shields.io/github/issues-closed/chiraag-kakar/managefunds?style=for-the-badge)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/chiraag-kakar/managefunds/pulls)
[![](https://img.shields.io/github/issues-pr/chiraag-kakar/managefunds?style=for-the-badge)]()
[![](https://img.shields.io/github/forks/chiraag-kakar/managefunds?style=for-the-badge)]()
[![](https://img.shields.io/github/stars/chiraag-kakar/managefunds?style=for-the-badge)]()

**Manage Funds** is a full stack web application where the users can manage Funds coming in their Programmes/Clubs/Organizations.


* They can add a fund along with the associated budget.
* Then they will also have the privilege to add expenses involved in that fund.
* The count of transactions and balance will be tracked too.

Note : For testing Django's unittest module is used

                                      😃Hit that ⭐ button to show some ❤️           

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites


```
Any Code Editor (VS Code preferred)
Python version 3.7 or higher
Latest version of Git
A PythonAnywhere Account (for deploying the project on a live system)
```

### Development Environment Setup : Windows


<details><summary>Step 1 : Downloading and Installing the Code Editor</summary>
 
 
| **Code Editor** | **Link** 	|
|-	|-	|
| Visual Studio Code 	| [Download it from here](https://code.visualstudio.com/)	|
| Sublime Text 3 	| [Download it from here](https://www.sublimetext.com/3) |
| Atom 	| [Download it from here](https://atom.io/)	|


</details>


---


<details><summary>Step 2 : Installing Python</summary>
 
 
* Click on [Download Python](https://www.python.org/downloads/windows/).
* Click on the "Latest Python 3 Release - Python x.x.x" link.
   * * Download the Windows x86-64 executable installer for 64-bit version of Windows
   * * Download the Windows x86 executable installer for 32-bit version of Windows.


* Make sure to check "Add Python 3.x to Path" in the setup window of the Installer.

Verify the installation from the command prompt using following command :
```
python --version
```
And the installed version of python will be printed.


</details>


---


<details><summary>Step 3 : Creating Project Directory </summary>


(Note : We are creating project directory in the desktop for easey and fast access)

```
cd desktop

mkdir myproject

cd myproject
```

</details>


---


<details><summary>Step 4 : Fork the Repository Cloning Repository using Git</summary>
 
 
```
git clone https://github.com/chiraag-kakar/managefunds.git
```


</details>


---


<details><summary>Step 5 : Creating Virtual Environment</summary>

Change the directory to the required one where the virtual environment will be created :
```
cd managefunds
```
Creating Virtual Environment named "vir" :
```
python -m venv vir
```
Activating "vir" :
```
vir\Scripts\activate
```
Command to deactivate "vir" :
```
deactivate
```


</details>


---


<details><summary>Step 6 : Installing Requirements</summary>


Note: Virtual Environment should be activated.


Upgrading pip to the latest version :
```
python -m pip install --upgrade pip
```


Installing requirements :
```
pip install -r requirements.txt
```


</details>


---


<details><summary>Step 7 : Creating Superuser and making database migrations to access the default Admin Panel</summary>
 
 
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```


</details>


---


<details><summary>Step 8 : Running the Project in local server</summary>


Note: Virtual Environment should be activated.


Run the following command in the terminal :
```
python manage.py runserver
```


</details>


## Congratulations for setting up the project locally.


## Contributing

* Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* For major changes, please open an [issue](https://github.com/chiraag-kakar/managefunds/issues) first to discuss what you would like to change.


Note : 
* Please take a moment to review the [Contributing.md]() and [Code of Conduct]() which provides the guidelines for contributing.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b <your_branch_name>`)
3. Stage your Changes (`git add .`) 
4. Commit your Changes (`git commit -m '<your_commit_message>'`)
5. Push to the Branch (`git push origin <your_branch_name>`)
6. Open a [Pull Request](https://github.com/chiraag-kakar/managefunds/pulls)


---

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/chiraag-kakar/managefunds/blob/master/LICENSE) file for details.

## AUTHOR : [Chiraag Kakar](https://github.com/chiraag-kakar)

