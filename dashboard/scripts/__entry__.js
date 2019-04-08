// dynamic imports are within functions so they don't happen until called
DMP_CONTEXT.loadBundle({

    "dashboard/index": () => [
        import(/* webpackMode: "eager" */ "./index.js"),
        import(/* webpackMode: "eager" */ "./../styles/index.css"),
    ],

    "dashboard/base_ajax": () => [
    ],

    "dashboard/app_base": () => [
    ],

})