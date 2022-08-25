package com.group5.opinionmanage.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

/**
 * @author 10569
 * @version 1.0
 * @description 数据库实体类
 * @Date 2022/8/24 14:17
 */

@Getter
@Setter

@Entity
@SuppressWarnings("JpaQlInspection")
@Table(name = "opinions")
public class Opinions {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer oid;

    private String context;

    private String type;

    private Integer feature;

    private String keyword;
    private Integer voteupcount;
    private Integer commentcount;
    private String questiontext;

    @Transient
    private Integer heat=0;

    public Integer getHeat() {
        return heat;
    }

    public void setHeat(Integer heat) {
        this.heat = heat;
    }

    public Opinions(String context, String type, Integer feature, String keyword, Integer voteupcount, Integer commentcount, String questiontext) {
        this.context = context;
        this.type = type;
        this.feature = feature;
        this.keyword = keyword;
        this.voteupcount = voteupcount;
        this.commentcount = commentcount;
        this.questiontext = questiontext;
        setHeat(commentcount * 2 + voteupcount);
    }

    public Integer getVoteupcount() {
        return voteupcount;
    }

    public void setVoteupcount(Integer voteupcount) {
        this.voteupcount = voteupcount;
        heat+=voteupcount;
    }

    public Integer getCommentcount() {
        return commentcount;
    }

    public void setCommentcount(Integer commentcount) {
        this.commentcount = commentcount;
        heat+=commentcount*2;
    }

    public String getQuestiontext() {
        return questiontext;
    }

    public void setQuestiontext(String questiontext) {
        this.questiontext = questiontext;
    }

    public Opinions() {
    }


    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Integer getFeature() {
        return feature;
    }

    public void setFeature(Integer feature) {
        this.feature = feature;
    }

    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public void setOid(Integer oid) {
        this.oid = oid;
    }


    public Integer getOid() {
        return oid;
    }
}


