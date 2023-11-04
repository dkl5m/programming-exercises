<!DOCTYPE html>
<html>
    <head>
        <title>Forms</title>
    </head>
    <body>
        <?php
            if(isset($_POST['action'])){
#                echo 'Post: '.$_POST['content'];
                echo $_FILES['archive']['name'];
            }
        ?>


<!--
        <form action="" method="post">
            <input type="text" name="name">
            <input type="hidden" name="key" value="1234">
            <textarea name="content"></textarea>
            <input type="submit" name="action" value="Send">
        </form>
        -->
 
        <form enctype="multipart/form-data" action="" method="post">
            <input type="file" name="archive">
            <input type="submit" name="action" value="Send">
        </form>
    </body>
</html>