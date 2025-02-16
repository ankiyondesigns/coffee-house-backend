document.addEventListener("DOMContentLoaded", function () {
    const editor = new EditorJS({
        holder: "editorjs",
        tools: {
            header: {
                class: Header,
                inlineToolbar: true,
                config: {
                    levels: [2, 3, 4],
                    defaultLevel: 2,
                },
            },
            image: {
                class: ImageTool,
                config: {
                    endpoints: {
                        byFile: "/upload-image/", // URL to handle image upload
                        byUrl: "/fetch-image/", // Optional: fetch image by URL
                    },
                },
            },
            video: {
                class: VideoTool,
                config: {
                    endpoints: {
                        byFile: "/upload-video/",
                        byUrl: "/fetch-video/",
                    },
                },
            },
            paragraph: {
                class: Paragraph,
                inlineToolbar: true,
            },
        },
        data: {}, // This will be filled when loading saved content
    });

    // Saving data before form submission
    document.querySelector("form").addEventListener("submit", function (event) {
        editor.save().then((outputData) => {
            document.getElementById("editorjs-data").value = JSON.stringify(outputData);
        });
    });
});
