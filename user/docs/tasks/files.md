# File Browser 

The File Browser is an integrated component within the web-based administrative console that enables users to explore, view, and manage files stored in the project’s repository, directly from the browser interface. 

The browser shows a full, unfiltered view of the project data store: differently from the catalog's view, the browser presents files organized in a tree, with nested folders and files. 

By default, every content registered in the catalog will be stored under a path resembling the following schema:

``/[entity]/[name]/[version]/..``


Do note that adding/moving/removing files from those paths will probably result in an inconsistent data layout: do it at your risk.


## Key Features



* **Hierarchical Navigation:**

Displays the repository’s directory structure in an expandable tree view, allowing users to easily browse folders and subfolders.

* **File Preview and Metadata**

Supports viewing file details such as name, size, type, modification date, and hash. Text-based files (e.g., .txt, .md, .json, .xml, .java) and images (*.png, .jpg) can be previewed inline within the console.

* **Contextual Actions:**

Users can perform actions such as download, upload on single or multiple files.

* **Access Control:**

The file browser respects user roles and permissions, ensuring only authorized users can modify or access certain files.

* **File sharing**

Users can generate read-only links to share files (and folders) with external collaborators.


## Exploring files

By opening the *File browser* users are presented with a familiar view showing the content of the storage.

TODO SCREENSHOT BROWSER


Navigation is performed by clicking on folder's names, or via the interactive breadcrumb.

When a single file is selected, the browser will show a contextual view with the file details and the available actions:

* **download** will initiate the file download via a temporary secure link
* **preview** will open the file's preview (for supported files)
* **share** will open the file sharing dialog
* **delete** will delete the file 

TODO SCREENSHOT FILE ASIDE


Under the actions toolbar the side view reports all the *metadata* available for the selected file:
* Name
* Path
* Content type
* Size
* Last modified (date)
* Hash (etag/md5/sha)


## File uploading

By opening the upload dialog from the toolbar, users are able to upload any kind of file to the project's repository. 

The uploader supports:
* a single file
* multiple files
* a folder


TODO SCREENSHOT FILE UPLOAD w/folder (multiple files)

By default, no limitations on file's size, content type or path are applied. Administrators may configure more restrictive conditions for specific environments.



## File sharing

Files stored in the project's repository are private by default: only members of the project can access the store. To enable external collaborators in downloading the files, the browser supports **file sharing** via temporay *pre-authorized* secure links.

Such links are generated with a signature derived from the user's credentials, and will expire after a configurable amount of time. 

Any user with the full link will be able to directly download the file: no specific client or code is required.

To share a file:

1. open the file details
2. click on the *share* button 
3. define the desired duration and click share
4. copy the link and send to users.

Do note that the generated secure link won't be shown again.