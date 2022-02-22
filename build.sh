#https://yingshaoxo.blogspot.com/2020/03/how-to-use-docker-to-build-kivy-to.html

export ANDROIDSDK="/home/code-flex-pc2/.buildozer/android/platform/android-sdk"
export ANDROIDNDK="/home/code-flex-pc2/.buildozer/android/platform/android-ndk-r19c"
export ANDROIDAPI="27"  # Target API version of your application
export NDKAPI="21"  # Minimum supported API version of your application

#p4a clean_builds
#p4a clean_dists
p4a apk --private . \
    --package=xyz.yingshaoxo.freedom \
    --name "Freedom" \
    --version 0.1 \
    --bootstrap=webview \
    --requirements=python3,eel,gevent,flask==1.1.4,flask_cors,itsdangerous==2.0.1,markupsafe==2.0.1 \
    --permission INTERNET --permission WRITE_EXTERNAL_STORAGE \
    --port=8888 --icon icon.png \
