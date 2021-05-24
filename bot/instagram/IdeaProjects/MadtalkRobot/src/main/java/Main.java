import com.github.instagram4j.instagram4j.IGClient;
import com.github.instagram4j.instagram4j.actions.story.StoryAction;
import com.github.instagram4j.instagram4j.exceptions.IGLoginException;
import com.github.instagram4j.instagram4j.models.media.reel.item.ReelMentionsItem;
import com.github.instagram4j.instagram4j.requests.media.MediaConfigureToStoryRequest;

import java.io.File;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {


        String username = args[0];
        String password = args[1];

        String file_src = args[2];
        String caption = "";

        if (args.length>3){
            caption = args[3];
        }

        if (args.length == 3){
            try {

                ReelMentionsItem item  = ReelMentionsItem.ReelMentionsItemBuilder;
                item.setUser_id("sir_behrad");
                MediaConfigureToStoryRequest configReq =
                        new MediaConfigureToStoryRequest("fds", Arrays.asList(item));
                IGClient client = IGClient.builder()
                        .username(username)
                        .password(password)
                        .login();

                client.actions()

                        .story()



                        .uploadPhoto(new File(file_src))
                        .thenAccept(response -> {
                            System.out.println("Successfully uploaded photo!");
                            System.exit(0);

                        })

                        .join();
            } catch (IGLoginException e) {
                e.printStackTrace();
            }
        }
        else {
            try {
                IGClient client = IGClient.builder()
                        .username(username)
                        .password(password)
                        .login();



                client.actions()

                        .timeline()





                        .uploadPhoto(new File(file_src),caption)
                        .thenAccept(response -> {

                            System.out.println("Successfully uploaded photo!");
                            System.exit(0);
                            return;
                        })

                        .join();
            } catch (IGLoginException e) {
                e.printStackTrace();
            }
        }



    }
}
