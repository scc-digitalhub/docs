# File Browser 

The File Browser is an integrated component within the web-based administrative console that enables users to explore, view, and manage files stored in the project’s repository, directly from the browser interface. 

The browser shows a full, unfiltered view of the project data store: differently from the catalog's view, the browser presents content organized in a tree, with nested folders and files. 

By default, every content registered in the catalog will be stored under a path resembling the following schema:

``/[entity]/[name]/[version]/..``

![File browser](../images/console/file-browser.png)

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

## Exploring Files

By opening the *Files* page from the left menu of the console, users are presented with a familiar view showing the content of the storage.

![File tree view](../images/console/file-tree-view.png)

Navigation is performed by clicking on folder names, or via the interactive breadcrumb.

When a single file is selected, the browser will show a contextual view with the file details. The following actions can be performed (when applicable) on the file via the corresponding buttons:

* **download**: initiate the file download via a temporary secure link
* **preview**: open the file's preview (for supported files)
* **share**: open the file sharing dialog
* **delete**: delete the file

![File details view](../images/console/file-details-view.png)

Under the actions toolbar the side view reports all the *metadata* available for the selected file:

* Name
* Path
* Content type
* Size
* Last modified (date)
* Hash (etag/md5/sha)

## File Uploading

The `UPLOAD` button on the top right of the File Browser opens a dialog for users to upload any kind of file to the project's repository. 

The uploader supports:

* a single file
* multiple files
* a folder

![File browser upload](../images/console/file-browser-upload.png)

By default, no limitations on file size, content type or path are applied. Administrators may configure more restrictive conditions for specific environments.

## File Sharing

Files stored in the project's repository are private by default: only members of the project can access the store. In order to enable file downloads by external collaborators, the browser supports **file sharing** via temporay *pre-authorized* secure links.

Such links are generated with a signature derived from the user's credentials, and will expire after a configurable amount of time. 

Any user with the full link will be able to directly download the file: no specific client or code is required.

To share a file:

1. open the file details
2. click on the `SHARE` button 
3. define the desired duration and click `SHARE`
4. copy the link and send to users.

Do note that the generated secure link won't be shown again.

![File sharing](../images/console/file-sharing.png)
