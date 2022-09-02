# ERPNext-Frepple Enhanced Integration
<a href="https://github.com/msf4-0/ERPNext-Frepple-Integration/blob/master/LICENSE">
    <img alt="GitHub" src="https://img.shields.io/github/license/msf4-0/ERPNext-Frepple-Integration.svg?color=blue">
</a>
<a href="https://github.com/msf4-0/ERPNext-Frepple-Integration/releases">
    <img alt="Releases" src="https://img.shields.io/github/release/msf4-0/ERPNext-Frepple-Integration?color=success" />
</a>
<a href="https://github.com/msf4-0/ERPNext-Frepple-Integration/releases">
    <img alt="Downloads" src="https://img.shields.io/github/downloads/msf4-0/ERPNext-Frepple-Integration/total.svg?color=success" />
</a>
<a href="https://github.com/msf4-0/ERPNext-Frepple-Integration/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/msf4-0/ERPNext-Frepple-Integration?color=blue" />
</a>
<a href="https://github.com/msf4-0/ERPNext-Frepple-Integration/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/msf4-0/ERPNext-Frepple-Integration?color=blue" />
</a>


## [Frepple](https://github.com/frePPLe/frepple) integration for [Frappe web framework](https://github.com/frappe/frappe)
Frepple Custom App built based on Frepple Advanced Planning and Scheduling software. It was built to integrate with ERPNext, act as a connector (middle station) that allow bidirectional data transfer between Frepple software and ERPNext. It is also used to map the data type between Frepple software and ERPNext since both software do not use the same data structure and format.


## Prerequisite
1. Installed the Frepple and successfully launched it on the localhost. Refer to [this document](https://docs.google.com/document/d/1P4U1rZszydwy2LmVAuC4lvYPl-dFw86LSC8Fz8zRsIE/edit?usp=sharing) for installing Frepple software.
2. Installed the ERPNext and successfully launched it on the localhost. Refer to [this github repository](https://github.com/msf4-0/IRPS-Enhanced-Frepple-Integration) to install ERPNext with Frepple integration app.

## The App Contains
1. All necessary Frepple software menus for production planning process.
<img width="865" alt="Frepple_doctype_pages" src="https://user-images.githubusercontent.com/108999556/188206023-0df12d25-06fa-43c3-af86-1a7059592e7b.png">

2. Import data from ERPNext to Frepple custom app with few clicks.
<img width="865" alt="Data_fetching_page" src="https://user-images.githubusercontent.com/108999556/188206235-815fd6ef-f54f-4678-b052-2c2c0c2c81d6.png">

3. Export data from Frepple custom app to Frepple software with few clicks.
<img width="865" alt="Data_export_page" src="https://user-images.githubusercontent.com/108999556/188206361-1324c458-aa6c-4ddc-b503-6ce8536ef112.png">

4. Generate the plan in Frepple custom app itself, with configurable constraints.
<img width="865" alt="Run_plan_page" src="https://user-images.githubusercontent.com/108999556/188206576-f1f16437-abb8-4f29-858d-6734bcc3929a.png">

5. Import manufacturing orders, purchase orders and distribution orders from Frepple software to ERPNext.
<img width="865" alt="Result_page" src="https://user-images.githubusercontent.com/108999556/188206692-c054bb55-0b29-44f5-958f-f091f3d3f9d5.png">

6. Embed Frepple page into ERPNext user interface using iframe. Access the frepple screens through `Frepple Custom Page`.
<img width="865" alt="Frepple custom page" src="https://user-images.githubusercontent.com/53387856/154400895-02414e51-bdbf-4c38-9861-98dbfd6eb425.png">

7. Generate work orders and purchase orders in ERPNext based on the result from Frepple.
<img width="865" alt="Frepple manufacturing order " src="https://user-images.githubusercontent.com/53387856/154401045-4a6ad63b-5583-41ee-b092-f5de0295698c.png">

8. Sync the status of work orders and purchase orders between ERPNext and Frepple.

## Installation
In order to install this integrated app into your ERPNext system, two major process must be done. These two process are described as following:

### I. Update ERPNext files
This is an important step where some of ERPNext files must be updated to accumodate the new version of Frepple custom app. To uodate these files, follow the instructions below:
1. Create a folder.

2. Open a Powershell terminal, navigate to the newly created folder.
3. Clone this repo.
    - `git clone https://`


### II. Install the new Frepple custom app into ERPNext:
1. Navigate to the bench directory by loging to <project_name>-erpnext-python-1 container. Run the folloing command:
> docker exec -it --user root <project_name>-erpnext-python-1 /bin/bash
- For example, `docker exec -it --user root project1-erpnext-python-1 /bin/bash`

2. By default, you will be in `~:/home/frappe/frappe-bench/sites` directory. Navigate out to `~:/home/frappe/frappe-bench` directory by typing:
> cd ..

3. Run the following command:
> bench get-app frepple https://github.com/msf4-0/ERPNext-Frepple-Enhanced-Integration.git

4. Install the app onto your site.
> bench --site <your.site.name> install-app frepple
- For example, `bench --site custom-erpnext-nginx install-app frepple`

5. Run bench start:
> bench start


## Frepple settings configuration
Before starting using Frepple custom app, you are required to set up certain information to enable the integration between ERPNext and Frepple.
Go to `Settings > Frepple Settings`.

- Authentication header:
> The Bearer web token key that required for REST API request. The key can be found in `Frepple Software`, under `Help > REST API Help`.

- Username and password:
> Username and password of superuser in Frepple. Default username and password are both “admin”. The information can also be found in `Frepple Software`, under `Admin > User`.


- URL:
> Web url that the user host the Frepple. The url is used for REST API request Get the wireless router IP address. You can find the Wireless LAN adapter Wi-Fi IPv4 address using `ipconfig` (Window OS) or `ifconfig` (Linux OS) command in the command prompt. E.g. http://192.168.112.1:5000.

- Frepple Integration:
> Checkbox. Tick it to turn on the automatic status syncing for sales order, work order, purchase order status and bin (stock) amount update.

- Secret key:
> Key is required for iframe embedded to render the Frepple page. Can be found under `etc/frepple/djangosettings.py` file.

## Important Note
Frepple custom app does not perform any data validation when the data are exported to Frepple software. The user must have basic knowledge of Frepple to ensure the data provided are sufficient to generate the plan in Frepple. A quick debug step is to verify the supply path matches the product structure. Remember to set up item supplier for the raw material.

## Contributors
1. [Drayang Chua Kai Yang](https://github.com/Drayang)
2. [Lee Xin Yue](https://github.com/leexy0)
3. [Chia Jun Shen](https://github.com/chiajunshen)


## License
This software is licensed under the [GNU GPLv3 LICENSE](/LICENSE) © [Selangor Human Resource Development Centre](http://www.shrdc.org.my/). 2021.  All Rights Reserved.

