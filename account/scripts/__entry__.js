// dynamic imports are within functions so they don't happen until called
DMP_CONTEXT.loadBundle({

    "account/index": () => [
        import(/* webpackMode: "eager" */ "./index.js"),
        import(/* webpackMode: "eager" */ "./../styles/index.css"),
    ],

    "account/sign-up": () => [
    ],

    "account/base_ajax": () => [
    ],

    "account/app_base": () => [
    ],

})