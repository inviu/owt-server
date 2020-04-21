// MIT License
//
// Copyright (c) 2012 Universidad Politécnica de Madrid
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

// Copyright (C) <2018> Intel Corporation
//
// SPDX-License-Identifier: Apache-2.0

// This file is borrowed from lynckia/licode with some modifications.

'use strict';
var conference;
var publicationGlobal;
const runSocketIOSample = function() {

    let localStream;
    let showedRemoteStreams = [];
    let myId;
    let subscriptionForMixedStream;
    let myRoom;

    function getParameterByName(name) {
        name = name.replace(/[\[]/, '\\\[').replace(/[\]]/, '\\\]');
        var regex = new RegExp('[\\?&]' + name + '=([^&#]*)'),
            results = regex.exec(location.search);
        return results === null ? '' : decodeURIComponent(results[1].replace(
            /\+/g, ' '));
    }

    var subscribeForward = getParameterByName('forward') === 'true'?true:false;
    var isSelf = getParameterByName('self') === 'false'?false:true;
    conference = new Owt.Conference.ConferenceClient();
    function createResolutionButtons(stream, subscribeResolutionCallback) {
        let $p = $(`#${stream.id}resolutions`);
        if ($p.length === 0) {
            $p = $(`<div id=${stream.id}resolutions> </div>`);
            $p.appendTo($('body'));
        }
        // Resolutions from settings.
        for (const videoSetting of stream.settings.video) {
            const resolution = videoSetting.resolution;
            if (resolution) {
                const button = $('<button/>', {
                    text: resolution.width + 'x' +
                        resolution.height,
                    click: () => {
                        subscribeResolutionCallback(stream, resolution);
                    }
                });
                button.prependTo($p);
            }
        }
        // Resolutions from extraCapabilities.
        for (const resolution of stream.extraCapabilities.video.resolutions.reverse()) {
            const button = $('<button/>', {
                text: resolution.width + 'x' +
                    resolution.height,
                click: () => {
                    subscribeResolutionCallback(stream, resolution);
                }
            });
            button.prependTo($p);
        };
        return $p;
    }
    function subscribeAndRenderVideo(stream){
        let subscirptionLocal=null;
        function subscribeDifferentResolution(stream, resolution){
            subscirptionLocal && subscirptionLocal.stop();
            subscirptionLocal = null;
            const videoOptions = {};
            videoOptions.resolution = resolution;
            //aoqi add
            videoOptions.codecs=[{"name":"h264"}];
            conference.subscribe(stream, {
                audio: true,
                video: videoOptions
            }).then((
                subscription) => {
                    subscirptionLocal = subscription;
                $(`#${stream.id}`).get(0).srcObject = stream.mediaStream;
            });
        }
        let $p = createResolutionButtons(stream, subscribeDifferentResolution);
        //aoqi add
        const videoOptions = {};
        videoOptions.codecs=[{"name":"h264"}];
        conference.subscribe(stream,{
            audio: true,
            video: videoOptions
        })
        .then((subscription)=>{
            subscirptionLocal = subscription;
            let $video = $(`<video controls autoplay id=${stream.id} style="display:block" >this browser does not supported video tag</video>`);
           $video.get(0).srcObject = stream.mediaStream;
           $p.append($video);
        }, (err)=>{ console.log('subscribe failed', err);
        });
        stream.addEventListener('ended', () => {
            removeUi(stream.id);
            $(`#${stream.id}resolutions`).remove();
        });
        stream.addEventListener('updated', () => {
            // Update resolution buttons
            $p.children('button').remove();
            createResolutionButtons(stream, subscribeDifferentResolution);
        });
    }
    function removeUi(id){
        $(`#${id}`).remove();
    }

    conference.addEventListener('streamadded', (event) => {
        console.log('A new stream is added ', event.stream.id);
        isSelf = isSelf?isSelf:event.stream.id != publicationGlobal.id;
        subscribeForward && isSelf && subscribeAndRenderVideo(event.stream);
        mixStream(myRoom, event.stream.id, 'common');
        event.stream.addEventListener('ended', () => {
            console.log(event.stream.id + ' is ended.');
        });
    });


    window.onload = function() {
        var simulcast = getParameterByName('simulcast') || false;
        var shareScreen = getParameterByName('screen') || false;
        myRoom = getParameterByName('room');
        var isHttps = (location.protocol === 'https:');
        var mediaUrl = getParameterByName('url');
        ///////aoqi add
        var rtmpUrl = getParameterByName('rtmp');
        var isPublish = getParameterByName('publish');
        var subscribeForward = getParameterByName('forward') === 'true'?true:false;

        // getRoom(myRoom,function(response){
        //     var roomInfo=response;
        //     var obj = JSON.parse(roomInfo)[0];
        //     obj.transcoding.video={
        //         parameters: {
        //             keyFrameInterval: true,
        //             bitrate: true,
        //             framerate: true,
        //             resolution: true
        //         },
        //         format: true
        //     }
        //     for (const index in obj.views) {
        //         obj.views[index].video.parameters.resolution.width=1920;
        //         obj.views[index].video.parameters.resolution.height=1080;
        //         //这个有什么用，拉流决定了接收格式
        //         // obj.views[index].video.format.codec="h264";
        //         // obj.views[index].video.format.profile="B";

        //         // obj.views[index].video.parameters.resolution.width=3840;
        //         // obj.views[index].video.parameters.resolution.height=2160;
        //     }
        //     //没硬件加速会议室无法使用M H h265
        //     obj.mediaIn.video=[
        //         {
        //             "codec": "h264"
        //         },
        //         {
        //             "codec": "h265"
        //         },
        //         {
        //             "codec": "vp8"
        //         },
        //         {
        //             "codec": "vp9"
        //         }
        //     ];
        //     obj.mediaOut.video.format=[
        //         {
        //             "codec": "vp8"
        //         },
        //         {
        //             "profile": "CB",
        //             "codec": "h264"
        //         },
        //         {
        //             "profile": "B",
        //             "codec": "h264"
        //         },
        //         // {
        //         //     "codec": "h265"
        //         // },
        //         {
        //             "codec": "vp9"
        //         }
        //     ];
        //     updateRoom(obj.id,obj);
        // });
        createToken(myRoom, 'user', 'presenter', function(response) {
            var token = response;
            conference.join(token).then(resp => {
                myId = resp.self.id;
                myRoom = resp.id;
            
                ///////aoqi add
                // getRoom(myRoom,function(response){
                //     var roomInfo=response;
                //     var obj = JSON.parse(roomInfo);
                    // obj.mediaOut.video.parameters.resolution=[
                    //     "x3/4",
                    //     "x2/3",
                    //     "x1/2",
                    //     "x1/3",
                    //     "x1/4",
                    //     "uhd_4k",
                    //     "hd1080p",
                    //     "hd720p",
                    //     "svga",
                    //     "vga",
                    //     "qvga",
                    //     "cif"
                    // ];
                //     updateRoom(myRoom,obj);
                // });
                //////
                if(mediaUrl){
                     startStreamingIn(myRoom, mediaUrl);
                }
                if (isPublish !== 'false') {
                    // audioConstraintsForMic
                    let audioConstraints = new Owt.Base.AudioTrackConstraints(Owt.Base.AudioSourceInfo.MIC);
                    // videoConstraintsForCamera
                    let videoConstraints = new Owt.Base.VideoTrackConstraints(Owt.Base.VideoSourceInfo.CAMERA);
                    if (shareScreen) {
                        // audioConstraintsForScreen
                        audioConstraints = new Owt.Base.AudioTrackConstraints(Owt.Base.AudioSourceInfo.SCREENCAST);
                        // videoConstraintsForScreen
                        videoConstraints = new Owt.Base.VideoTrackConstraints(Owt.Base.VideoSourceInfo.SCREENCAST);
                    }

                    ///////aoqi add
                    videoConstraints.resolution=new Owt.Base.Resolution(640,480);
                    // videoConstraints.resolution=new Owt.Base.Resolution(800,600);
                    // videoConstraints.resolution=new Owt.Base.Resolution(1280,720);
                    // videoConstraints.resolution=new Owt.Base.Resolution(1920,1080);
                    //////
                    let mediaStream;
                    Owt.Base.MediaStreamFactory.createMediaStream(new Owt.Base.StreamConstraints(
                        audioConstraints, videoConstraints)).then(stream => {
                        let publishOption;
                        if (simulcast) {
                            publishOption = {video:[
                                {rid: 'q', active: true/*, scaleResolutionDownBy: 4.0*/},
                                {rid: 'h', active: true/*, scaleResolutionDownBy: 2.0*/},
                                {rid: 'f', active: true}
                            ]};
                        }
                        else{
                            //aoqi add
                            //调整发送码率
                            // publishOption={video:[
                            //     {codec:{name:'vp8'},maxBitrate:4000}
                            // ]};
                            //推h264
                            publishOption={video:[
                                {codec:{name:'h264',profile:'B'}}
                            ]};
                        }
                        mediaStream = stream;
                        localStream = new Owt.Base.LocalStream(
                            mediaStream, new Owt.Base.StreamSourceInfo(
                                'mic', 'camera'));
                        $('.local video').get(0).srcObject = stream;
                        conference.publish(localStream, publishOption).then(publication => {
                            publicationGlobal = publication;
                            ///////aoqi add
                            // if(!subscribeForward)
                            {
                                mixStream(myRoom, publication.id, 'common')
                            }
                            ///////aoqi add
                            if(rtmpUrl){
                                startStreamingOut(myRoom, publication.id,rtmpUrl)
                            }
                            publication.addEventListener('error', (err) => {
                                console.log('Publication error: ' + err.error.message);
                            });
                        });
                    }, err => {
                        console.error('Failed to create MediaStream, ' +
                            err);
                    });
                }
                var streams = resp.remoteStreams;
                for (const stream of streams) {
                    if(!subscribeForward){
                      if (stream.source.audio === 'mixed' || stream.source.video ===
                        'mixed') {
                        subscribeAndRenderVideo(stream);
                      }
                    } else if (stream.source.audio !== 'mixed') {
                        subscribeAndRenderVideo(stream);
                    }
                }
                console.log('Streams in conference:', streams.length);
                var participants = resp.participants;
                console.log('Participants in conference: ' + participants.length);
            }, function(err) {
                console.error('server connection failed:', err);
                if (err.message.indexOf('connect_error:') >= 0) {
                    const signalingHost = err.message.replace('connect_error:', '');
                    const signalingUi = 'signaling';
                    removeUi(signalingUi);
                    let $p = $(`<div id=${signalingUi}> </div>`);
                    const anchor = $('<a/>', {
                        text: 'Click this for testing certificate and refresh',
                        target: '_blank',
                        href: `${signalingHost}/socket.io/`
                    });
                    anchor.appendTo($p);
                    $p.appendTo($('body'));
                }
            });
        });
    };
};
window.onbeforeunload = function(event){
    conference.leave()
    publicationGlobal.stop();
}
